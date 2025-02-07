document.addEventListener('DOMContentLoaded', () => {
    const title = document.getElementById('title');
    const locationMenu = document.getElementById('location-menu');
    const specialistsMenu = document.getElementById('specialists-menu');
    const reviewsMenu = document.getElementById('reviews-menu');
    const contactMenu = document.getElementById('contact-menu');
    const paymentMenu = document.getElementById('payment-menu');
    const faqMenu = document.getElementById('faq-menu');
    const specialists = document.getElementById('specialists');
    const reviews = document.getElementById('reviews');
    const contact = document.getElementById('contact');
    const payment = document.getElementById('payment');
    const faq = document.getElementById('faq');
    const heroTitle = document.getElementById('hero-title');
    const appointmentElements = document.querySelectorAll('.appointment-buttons');
    const locationButtons = document.querySelectorAll('.location-button');
    const heroParagraph = document.getElementById('hero-paragraph');
    const aboutTitle = document.getElementById('about-title');
    const aboutParagraph = document.getElementById('about-paragraph');
    const aboutVideo = document.getElementById('about-video-title');
    const locationTitle = document.getElementById('location-title');
    const locationParagraph= document.getElementById('location-paragraph');



    let languageObtain = navigator.language;
    const browserLanguage = languageObtain.split('-')[0];
    console.log(browserLanguage);

    const loadContent=(language)=>{
        fetch(CONTENT_URL)
        .then(response=>response.json())
        .then(data => {
            title.textContent=data[language].title;
            locationMenu.textContent=data[language].locationMenu;
            specialistsMenu.textContent=data[language].specialistsMenu;
            reviewsMenu.textContent=data[language].reviewsMenu;
            contactMenu.textContent=data[language].contactMenu;
            paymentMenu.textContent=data[language].paymentMenu;
            faqMenu.textContent=data[language].faqMenu;
            location.textContent=data[language].locationMenu;
            specialists.textContent=data[language].specialistsMenu;
            reviews.textContent=data[language].reviewsMenu;
            contact.textContent=data[language].contactMenu;
            payment.textContent=data[language].paymentMenu;
            faq.textContent=data[language].faqMenu;
            heroTitle.textContent=data[language].heroTitle;
            appointmentElements.forEach(element => {
                element.textContent=data[language].appointmentElements;
            })
            locationButtons.forEach(element => {
                element.textContent=data[language].locationButtons;
            })
            heroParagraph.textContent=data[language].heroParagraph;
            aboutTitle.textContent=data[language].aboutTitle;
            aboutParagraph.textContent=data[language].aboutParagraph;
            aboutVideo.textContent=data[language].aboutVideo;
            locationTitle.textContent=data[language].locationTitle;
            locationParagraph.textContent=data[language].locationParagraph;
        })
    }




    loadContent(browserLanguage);
    
    const spanishSelectorElements = document.querySelectorAll('.selector-es');
    const englishSelectorElements = document.querySelectorAll('.selector-en'); 


    //Selector browser settings
    const languageSelector = (browserLanguage) => {           
        if(browserLanguage === 'es'){
            spanishSelectorElements.forEach(element => {
                element.classList.add('hidden');
                englishSelectorElements.forEach(elementEnglish => {
                    elementEnglish.classList.remove('hidden');
                })
            })
        }
        if(browserLanguage === 'en'){
            englishSelectorElements.forEach(element => {
                element .classList.add('hidden');
                spanishSelectorElements.forEach(element => {
                    element.classList.remove('hidden');
                })
            })
        }
    }

    languageSelector(browserLanguage)

    //Selectores 
    spanishSelectorElements.forEach(element => {
        element.addEventListener('click', () => {
            loadContent('es');
            
        })
    })

    englishSelectorElements.forEach(element => {
        element.addEventListener('click', () => {
            loadContent('en');
            element.classList.add('hidden');
            spanishSelectorElements.forEach(element => {
                element.classList.remove('hidden');
            })
        })
    })
    
    spanishSelectorElements.forEach(element => {
        element.addEventListener('click', () => {
            loadContent('es');
            element.classList.add('hidden');
            englishSelectorElements.forEach(element => {
                element.classList.remove('hidden');
            })
        })
    })
})