let html_element = document.documentElement;
let theme_btn = document.getElementById("themeToggleBtn");
let theme_icon = document.getElementById("themeToggleIcon");
let default_theme = 'light';

// set default theme
html_element.setAttribute('data-bs-theme', default_theme);

// toggle on click betwen light/dark mode
theme_btn.addEventListener('click', function(){
    let current_theme = html_element.getAttribute('data-bs-theme');
    let next_theme;

    if (current_theme === 'light') {
        next_theme = 'dark';
        theme_icon.textContent = '🌙';
    } else {
        next_theme = 'light';
        theme_icon.textContent = '🔆';
    }

    html_element.setAttribute('data-bs-theme', next_theme);
})