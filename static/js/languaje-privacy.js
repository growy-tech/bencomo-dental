addEventListener('DOMContentLoaded', () =>{
    const title = document.getElementById('title');
    const paragraph = document.getElementById('paragraph');
    const backButton = document.getElementById('back-button');

    let languageObtain = navigator.language;
    const browserLanguage = languageObtain.split('-')[0];
    
    console.log(browserLanguage);
    const loadContent=(language)=>{
        fetch(CONTENT_URL)
        .then(response=>response.json())
        .then(data => {

            title.textContent=data[language].title;
            paragraph.textContent=data[language].paragraph;
            backButton.textContent=data[language].backButton;
        })
    }

    loadContent(browserLanguage); 

})