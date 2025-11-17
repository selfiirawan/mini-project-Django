let html_element = document.documentElement;
let theme_btn = document.getElementById("themeToggleBtn");
let default_theme = 'light';

console.log("theme btn: ", theme_btn);

// set default theme
html_element.setAttribute('data-bs-theme', default_theme);

// toggle on click betwen light/dark mode
theme_btn.addEventListener('click', function(){
    let current_theme = html_element.getAttribute('data-bs-theme');
    let next_theme;

    if (current_theme === 'light') {
        next_theme = 'dark';
    } else {
        next_theme = 'light';
    }

    html_element.setAttribute('data-bs-theme', next_theme);
})