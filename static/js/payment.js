document.addEventListener('DOMContentLoaded', () => {
    

    let languageObtain = navigator.language;
    const browserLanguage = languageObtain.split('-')[0];
    console.log(browserLanguage);

    const paymentLink = document.getElementById('payment-link');

    if(browserLanguage === 'es'){
        paymentLink.setAttribute('href','https://buy.stripe.com/bIY3epgiB85x70kdQR') ;
    } if(browserLanguage === 'en'){
        paymentLink.setAttribute('href', 'https://buy.stripe.com/eVa16h2rL71t1G07ss')
    }
})