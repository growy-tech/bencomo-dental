document.addEventListener('DOMContentLoaded', () => {
    const contactForm = document.getElementById('contact-form');
    const suggestionForm = document.getElementById('suggestions-form');
    const suggestionButton = document.getElementById('suggestion-text');

    suggestionButton.addEventListener('click', () =>{
        contactForm.classList.toggle('hidden');
        suggestionForm.classList.toggle('hidden');
    })
    
})