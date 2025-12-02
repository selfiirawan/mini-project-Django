// let html_element = document.documentElement;
// let theme_btn = document.getElementById("themeToggleBtn");
// let theme_icon = document.getElementById("themeToggleIcon");
// let default_theme = 'light';

// // set default theme
// html_element.setAttribute('data-bs-theme', default_theme);

// // toggle on click betwen light/dark mode
// theme_btn.addEventListener('click', function(){
//     let current_theme = html_element.getAttribute('data-bs-theme');
//     let next_theme;

//     if (current_theme === 'light') {
//         next_theme = 'dark';
//         theme_icon.textContent = '🌙';
//     } else {
//         next_theme = 'light';
//         theme_icon.textContent = '🔆';
//     }

//     html_element.setAttribute('data-bs-theme', next_theme);
// })

// NEW CODE 
let html_element = document.documentElement;
let theme_btn = document.getElementById("themeToggleBtn");
let theme_icon = document.getElementById("themeToggleIcon");

// 1 - Load saved theme (if any) from localStorage
let saved_theme = localStorage.getItem("theme");

// If no saved theme, set default to light mode 
let current_theme = saved_theme ? saved_theme : 'light';

// Apply theme on page load 
html_element.setAttribute('data-bs-theme', current_theme);

// Set icon based on current theme
theme_icon.textContent = current_theme === "light" ? "🔆" : "🌙";


// 2 - Toggle on click between light/dark mode 
theme_btn.addEventListener("click", function() {
    let current = html_element.getAttribute("data-bs-theme");
    let next_theme;

    if (current === "light") {
        next_theme = "dark";
        theme_icon.textContent = "🌙";
    } else {
        next_theme = "light";
        theme_icon.textContent = "🔆";
    }

    // Apply the new theme
    html_element.setAttribute("data-bs-theme", next_theme);

    // 3 - Save the selected theme to localStorage
    localStorage.setItem("theme", next_theme);
})