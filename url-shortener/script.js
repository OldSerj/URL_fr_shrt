const input = document.getElementById('url-input');
const button = document.getElementById('shorten-btn');
const toggleDark = document.getElementById('toggle-dark');
let alreadyShortened = false;

button.addEventListener('click', () => {
    const url = input.value.trim();

    if (!url || alreadyShortened) return;

    fetch('/shorten', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ url })
    })
    .then(response => response.json())
    .then(data => {
        input.value = data.shortened_url;
        alreadyShortened = true;
    })
    .catch(error => console.error('Error:', error));
});

// placeholder disappears automatically when typing (default behavior)

// Toggle dark mode
toggleDark.addEventListener('click', () => {
    document.body.classList.toggle('dark-mode');
});
