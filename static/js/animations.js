window.addEventListener('DOMContentLoaded', (event) => {
    const heroImage = document.getElementById('hero-img');
    const hero = document.getElementById('hero');
    heroImage.classList.remove('opacity-0');
    heroImage.classList.add('opacity-100');
    hero.classList.remove('opacity-0');
    hero.classList.add('opacity-100');
})

