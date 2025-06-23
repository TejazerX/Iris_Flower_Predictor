## 🌸 AI-Powered Iris Flower Classifier

A sleek, interactive web app that uses a trained **deep learning model** to classify Iris flower species based on user-provided sepal and petal measurements. Built with **Flask**, **Keras**, and **Matplotlib**, this project demonstrates how machine learning models can be deployed in real-world web environments.

---

### 🚀 Features

* ✅ Deep learning model built using **TensorFlow/Keras**
* ✅ Web interface built with **Flask**
* ✅ **Bar chart** visualizing prediction probabilities
* ✅ **Animated prediction results**
* ✅ **Dark mode toggle** for improved readability
* ✅ Responsive design with Bootstrap and custom CSS

---

### 📊 How It Works

1. User inputs sepal/petal length and width
2. The app sends the data to a pre-trained Keras model
3. The model predicts the class probabilities (Setosa, Versicolor, Virginica)
4. The prediction and a **bar chart** are displayed on the page

---

### 🧠 Machine Learning Details

* **Dataset**: [Iris Dataset](https://archive.ics.uci.edu/ml/datasets/iris)
* **Algorithm**: Multi-class classification using a simple feedforward neural network
* **Frameworks**: `TensorFlow`, `Keras`, `sklearn`

---

### 📁 Project Structure

```
Iris_webapp/
├── app.py                     # Flask backend
├── iris_model.h5              # Trained ML model
├── templates/
│   └── index.html             # Frontend HTML
├── static/
│   ├── style.css              # Custom CSS
│   └── script.js              # Dark mode toggle
└── README.md
```

---

### ⚙️ Setup Instructions

1. **Clone the repo**

   ```bash
   git clone https://github.com/your-username/iris-webapp.git
   cd iris-webapp
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**

   ```bash
   python app.py
   ```

4. Open your browser and go to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

### 📦 Requirements

You can create a `requirements.txt` with:

```txt
flask
tensorflow
matplotlib
numpy
scikit-learn
```

Install with:

```bash
pip install -r requirements.txt
```

---
<!--
### 📸 Screenshot

![Screenshot of webapp](https://user-images.githubusercontent.com/your-username/placeholder.png)

---
-->
### 📚 Learnings

* How to train and save a deep learning model
* How to deploy ML models using Flask
* UI/UX design with Bootstrap, dark mode, and custom CSS
* Data visualization using Matplotlib + base64 images

---

### 🙌 Credits

* Iris dataset: UCI Machine Learning Repository
* Flask, TensorFlow, Bootstrap, Matplotlib

---
