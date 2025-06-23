/* ---------- dark-mode handling ---------- */
const switchEl = document.getElementById('darkSwitch');
const bodyEl   = document.body;

// init: read preference
const savedMode = localStorage.getItem('irisDarkMode');
if (savedMode === 'on') { bodyEl.classList.add('dark-mode'); switchEl.checked = true; }

switchEl.addEventListener('change', () => {
    if (switchEl.checked) {
        bodyEl.classList.add('dark-mode');
        localStorage.setItem('irisDarkMode','on');
    } else {
        bodyEl.classList.remove('dark-mode');
        localStorage.setItem('irisDarkMode','off');
    }
});
