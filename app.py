from flask import Flask, render_template, request
import numpy as np
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt
import io, base64

app = Flask(__name__)
model      = load_model("iris_model.h5")
class_map  = ['Setosa', 'Versicolor', 'Virginica']

# ---------- helper: draw bar & return base64 ----------
def get_bar_chart(prob):

    fig, ax = plt.subplots(figsize=(5, 2))
    species = ['Setosa', 'Versicolor', 'Virginica']
    colors = ['#ff9999', '#66b3ff', '#99ff99']

    ax.barh(species, prob, color=colors)
    ax.set_xlim(0, 1)
    ax.set_xlabel("Probability")
    ax.set_title("Prediction Probabilities")
    for i, v in enumerate(prob):
        ax.text(v + 0.02, i, f"{v:.2f}", color='black', va='center')

    plt.tight_layout()
    buf = io.BytesIO()
    plt.savefig(buf, format='png', transparent=True)
    buf.seek(0)
    img_b64 = base64.b64encode(buf.read()).decode('utf-8')
    plt.close(fig)
    return img_b64

# ------------------------------------------------------

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        vals      = [float(request.form[k]) for k in
                     ('sepal_length', 'sepal_width', 'petal_length', 'petal_width')]
        prob      = model.predict(np.array([vals]))[0]
        species   = class_map[int(np.argmax(prob))]
        chart_b64 = get_bar_chart(prob)
        return render_template('index.html',
                               prediction = species,
                               chart      = chart_b64,
                               prob       = [round(p*100,1) for p in prob])
    except Exception as e:
        return render_template('index.html', prediction=f"Error: {e}")

if __name__ == '__main__':
    app.run(debug=True)
