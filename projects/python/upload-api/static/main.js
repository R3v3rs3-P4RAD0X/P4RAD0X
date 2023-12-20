// A function that is called when the page is loaded
function main() {
    // Log that the page has loaded
    console.log('Page loaded');

    // Check if the user is using dark mode
    if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
        // If the user is using dark mode, set the theme to dark
        setTheme('dark');
    }
}

// Set the theme of the page
function setTheme(theme) {
    // Get the .container element
    let container = document.querySelector('.container');
    let navigation = document.querySelector('.container main nav');
    let navigationLinks = document.querySelectorAll('.container main nav ul li a');
    let uploadFormDiv = document.querySelector(".container main div.form");
    let uploadForm = document.querySelector(".container main div.form form");
    let files = document.querySelectorAll(".container main div.files ul li div.file");

    // Create an array of all the elements
    let elements = [container, navigation, ...navigationLinks, uploadFormDiv, uploadForm, ...files];

    // Iterate over all the elements
    for (let element of elements) {
        // Check if the element exists
        if (element) {
            // Check if the element has the class dark-mode or light-mode
            if (element.classList.contains('dark-mode') || element.classList.contains('light-mode')) {
                // If the element has the class dark-mode or light-mode, remove it
                element.classList.remove('dark-mode');
                element.classList.remove('light-mode');
            }

            // Check if the element has the selected-page class
            if (element.classList.contains('selected-page')) {
                // Continue to the next iteration
                continue;
            }

            // Add the new theme class
            element.classList.add(theme + '-mode');
        }
    }
}

// On page load, call the main function
window.addEventListener('load', main);