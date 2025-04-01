
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
    const contact = document.getElementById('contact');;
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
    const directionsBtn = document.getElementById('directions-btn');
    const specialistsTitle = document.getElementById('our-specialists');
    const doctorTitleFemale = document.querySelectorAll('.doctor-title-female');
    const doctorTitleMale = document.querySelectorAll('.doctor-title-male');
    const doctorDesOne = document.getElementById('doctor-des-1');
    const doctorDesTwo = document.getElementById('doctor-des-2');
    const doctorDesThree = document.getElementById('doctor-des-3');
    const doctorDesFour = document.getElementById('doctor-des-4');
    const doctorDesSix = document.getElementById('doctor-des-6');
    const doctorDesSeven = document.getElementById("doctor-des-7");
    const testimonyTitle = document.getElementById('testimony-title');
    const testimonyOne = document.getElementById('testimony-1-paragraph');
    const testimonyTwo = document.getElementById('testimony-2-paragraph');
    const testimonyThree = document.getElementById('testimony-3-paragraph');
    const testimonyFour = document.getElementById('testimony-4-paragraph');
    const testimonyFive = document.getElementById('testimony-5-paragraph');
    const testimonySix = document.getElementById('testimony-6-paragraph');
    const testimonySeven = document.getElementById('testimony-7-paragraph');
    const testimonyEight = document.getElementById('testimony-8-paragraph');
    const testimonyNine = document.getElementById('testimony-9-paragraph');
    const testimonyTen = document.getElementById('testimony-10-paragraph');
    const testimonyEleven = document.getElementById('testimony-11-paragraph');
    const testimonyTwelve = document.getElementById('testimony-12-paragraph');
    const testimonyThirteen =document.getElementById('testimony-13-paragraph');
    const testimonyFourteen = document.getElementById('testimony-14-paragraph');
    const viaFacebook = document.querySelectorAll('.via-facebook');
    const viaGoogle = document.querySelectorAll('.via-google');
    const testimonyImgTitle = document.getElementById('testimony-img-title');
    const testimonyImgSub = document.getElementById('picture-paragraph');
    const testimonyVideoTitle = document.getElementById('testimony-video-title');
    const testimonyVideoParagraph = document.getElementById('testimony-video-paragraph');
    const lightParagraphOne = document.getElementById('light-paragraph');
    const lightParagraphTwo = document.getElementById('light-paragraph-2');
    const paymentTitle = document.getElementById('payment-title');
    const cashText = document.getElementById('cash-text');
    const cardText = document.getElementById('card-text');
    const transferText = document.getElementById('transfer-text');
    const stripeText = document.getElementById('stripe-text');
    const paymentInfoTitle = document.getElementById('info-payment-title');
    const paymentInfoParagraph = document.getElementById('info-payment-paragraph');
    const paymentInfoParagraphTwo = document.getElementById('info-payment-paragraph-2');
    const contactTitle = document.getElementById('contact-title');
    const contactParagraph = document.getElementById('contact-paragraph');
    const contactName = document.getElementById('name-text');
    const contactEmail = document.getElementById('email-text');
    const contactPhone = document.getElementById('phone-text');
    const contactMsg = document.getElementById('msg-text');
    const contactSend = document.getElementById('send-text');
    const socialTitle = document.getElementById('social-title');
    const facebookText = document.getElementById('facebook-text');
    const instagramText = document.getElementById('instagram-text');
    const messageText = document.getElementById('message-text');
    const whatsappText = document.getElementById('whatsapp-text');
    const faqTitle = document.getElementById('faq-title');
    const faq1Title = document.getElementById('faq-1-title');
    const days1 = document.getElementById('days-1');
    const daySaturday = document.getElementById('day-saturday');
    const faq2Title = document.getElementById('faq-2-title');
    const faq2Content = document.getElementById('faq-2-content');
    const faq3Title = document.getElementById('faq-3-title');
    const faq3Content = document.getElementById('faq-3-content');
    const faq3Content2 = document.getElementById('faq-3-content-2');
    const followUsText = document.getElementById('follow-us-text');
    const siteText = document.getElementById('site-text');
    const locationFooter = document.getElementById('location-footer');
    const aboutUsFooter = document.getElementById('about-us-footer');
    const appointmentFooter = document.getElementById('appointment-footer');
    const specialistsFooter = document.getElementById('specialists-footer');
    const paymentFooter = document.getElementById('payment-footer');
    const contactFooter = document.getElementById('contact-footer');
    const testimoniesFooter = document.getElementById('testimonies-footer');
    const growyText = document.getElementById('growy-text');
    const paymentLink = document.querySelectorAll('.payment-link');
    const paymentAnchor = document.querySelectorAll('.payment-anchor');
    const testimonyVideoOne = document.getElementById('testimony-video');
    const suggestionText = document.getElementById('suggestion-text');
    const formPacienteName = document.getElementById('name-text-suggestions');
    const formSuggestionPhone = document.getElementById('phone-text-suggestion');
    const formPacientText = document.getElementById('msg-text-suggestion');
    const formSuggestionsTitle = document.getElementById('contact-title-suggestions');
    const formSuggestionsSubTitle = document.getElementById('contact-paragraph-suggestions');
    const suggestionSend = document.getElementById('send-suggestion');
    //Memberships section
    const membershipsTitle = document.getElementById('memberships-title');
    const membershipsSubtitle = document.getElementById('memberships-subtitle');
    const membershipIndividualTitle = document.getElementById('membership-individual-name');
    const membershipFamiliarTitle = document.getElementById('membership-familiar-name');
    const yearlyRenewal = document.querySelectorAll('.yearly-renewal-text');
    const membershipsFamilySpecs = document.getElementById('memberships-family-specs');
    const benefitsDiagnostics = document.querySelectorAll('.benefit-complet-diagnostics');
    const benefitNoCost= document.querySelectorAll('.benefit-no-cost');
    const benefitDentalCleanings = document.querySelectorAll('.benefit-dental-cleanings');
    const benefitTwoCleanings = document.querySelectorAll('.benefit-two-cleanings');
    const benefitBlank = document.querySelectorAll('.benefit-blank');
    const benefitFifty= document.querySelectorAll('.benefit-fifty-percent');
    const benefitsThreatments = document.querySelectorAll('.benefit-treatments-discount');
    const benefitFinancialPlans = document.querySelectorAll('.benefit-finacial-plans');
    const membershipBuyButtons = document.querySelectorAll('.memberships-buy-btn');

    console.log(benefitNoCost);
    console.log(benefitsDiagnostics);



//deploy

    let languageObtain = navigator.language;
    const browserLanguage = languageObtain.split('-')[0];

    const loadContent=(language)=>{
        fetch(CONTENT_URL)
        .then(response=>response.json())
        .then(data => {
            //Memberships Section
            membershipIndividualTitle.textContent=data[language].membershipIndividualTitle;
            membershipsTitle.textContent=data[language].membershipsTitle;
            membershipsSubtitle.textContent=data[language].membershipsSubtitle;
            membershipFamiliarTitle.textContent=data[language].membershipFamiliarTitle;
            yearlyRenewal.forEach(element => {
                element.textContent=data[language].yearlyRenewal;
            })
            membershipsFamilySpecs.textContent=data[language].membershipsFamilySpecs;
            benefitsDiagnostics.forEach(element => {
                element.childNodes[0].textContent=data[language].benefitsDiagnostics;
            })
            benefitNoCost.forEach(element => {
                element.textContent=data[language].benefitNoCost;
            })
            benefitDentalCleanings.forEach(element => {
                element.childNodes[1].textContent=data[language].benefitDentalCleanings;
            })
            benefitTwoCleanings.forEach(element => {
                element.textContent=data[language].benefitTwoCleanings;
            })
            benefitBlank.forEach(element => {
                element.childNodes[0].textContent=data[language].benefitBlank;
            })
            benefitFifty.forEach(element => {
                element.textContent=data[language].benefitFifty;
            })
            benefitsThreatments.forEach(element => {
                element.childNodes[0].textContent=data[language].benefitsThreatments;
                element.childNodes[1].textContent=data[language].benefitsThreatmentsTwo;
                element.childNodes[2].textContent=data[language].benefitsThreatmentsThree;
            })
            benefitFinancialPlans.forEach(element => {
                element.childNodes[0].textContent=data[language].benefitFinancialPlans;
                element.childNodes[1].textContent=data[language].benefitFinancialPlansTwo;
            })

            membershipBuyButtons.forEach(element => {
                element.textContent=data[language].membershipBuyButtons
            })            

            suggestionSend.textContent=data[language].contactSend;
            formSuggestionsSubTitle.textContent=data[language].formSuggestionsSubTitle;
            formSuggestionsTitle.textContent=data[language].formSuggestionsTitle;
            formPacientText.textContent=data[language].formPacientText
            formPacienteName.textContent=data[language].formPacienteName;
            formSuggestionPhone.textContent=data[language].contactPhone;
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
            directionsBtn.textContent=data[language].directionsButtons;
            specialistsTitle.textContent=data[language].specialistsTitle;
            doctorTitleFemale.forEach(element => {
                element.textContent=data[language].doctorTitleFemale;
            })
            doctorTitleMale .forEach(element => {
                element.textContent=data[language].doctorTitleMale
            })
            doctorDesOne.textContent=data[language].doctorDesOne;
            doctorDesTwo.textContent=data[language].doctorDesTwo;
            doctorDesThree.textContent=data[language].doctorDesThree;
            doctorDesFour.textContent=data[language].doctorDesFour;
            doctorDesSix.textContent=data[language].doctorDesSix;
            doctorDesSeven.textContent=data[language].doctorDesSeven;
            testimonyTitle.textContent=data[language].testimonyTitle;
            testimonyOne.textContent=data[language].testimonyOne;
            testimonyTwo.textContent=data[language].testimonyTwo;
            testimonyThree.textContent=data[language].testimonyThree;
            testimonyFour.textContent=data[language].testimonyFour;
            testimonyFive.textContent=data[language].testimonyFive;
            testimonySix.textContent=data[language].testimonySix;
            testimonySeven.textContent=data[language].testimonySeven;
            testimonyEight.textContent=data[language].testimonyEight;
            testimonyNine.textContent=data[language].testimonyNine;
            testimonyTen.textContent=data[language].testimonyTen;
            testimonyEleven.textContent=data[language].testimonyEleven;
            testimonyTwelve.textContent=data[language].testimonyTwelve;
            testimonyThirteen.textContent=data[language].testimonyThirteen;
            testimonyFourteen.textContent=data[language].testimonyFourteen;

            viaFacebook.forEach(element => {
                element.textContent=data[language].viaFacebook;
            })
            viaGoogle.forEach(element => {
                element.textContent=data[language].viaGoogle;
            })
            testimonyImgTitle.textContent=data[language].testimonyImgTitle;
            testimonyImgSub.textContent=data[language].testimonyImgSub;
            testimonyVideoTitle.textContent=data[language].testimonyVideoTitle;
            testimonyVideoParagraph.textContent=data[language].testimonyVideoParagraph;
            lightParagraphOne.textContent=data[language].lightParagraphOne;
            lightParagraphTwo.textContent=data[language].lightParagraphTwo;
            paymentTitle.textContent=data[language].paymentTitle;
            cashText.textContent=data[language].cashText;
            cardText.textContent=data[language].cardText;
            transferText.textContent=data[language].transferText;
            stripeText.textContent=data[language].stripeText;
            paymentInfoTitle.textContent=data[language].paymentInfoTitle;
            paymentInfoParagraph.textContent=data[language].paymentInfoParagraph;
            paymentInfoParagraphTwo.textContent=data[language].paymentInfoParagraphTwo;
            contactTitle.textContent=data[language].contactTitle;
            contactParagraph.textContent=data[language].contactParagraph;
            contactName.textContent = data[language].contactName;
            contactPhone.textContent = data[language].contactPhone;
            contactMsg.textContent = data[language].contactMsg;
            contactSend.textContent = data[language].contactSend;
            contactEmail.textContent = data[language].contactEmail;
            socialTitle.textContent = data[language].socialTitle;
            facebookText.textContent = data[language].facebookText;
            instagramText.textContent = data[language].instagramText;
            messageText.textContent = data[language].messageText;
            whatsappText.textContent = data[language].whatsappText;
            faqTitle.textContent = data[language].faqTitle;
            faq1Title.textContent = data[language].faq1Title;
            days1.textContent = data[language].days1;
            daySaturday.textContent = data[language].daySaturday;
            faq2Title.textContent = data[language].faq2Title;
            faq2Content.textContent = data[language].faq2Content;
            faq3Title.textContent = data[language].faq3Title;
            faq3Content.textContent = data[language].faq3Content;
            faq3Content2.textContent = data[language].faq3Content2;
            followUsText.textContent = data[language].followUsText;
            siteText.textContent = data[language].siteText;
            locationFooter.textContent = data[language].locationFooter;
            aboutUsFooter.textContent = data[language].aboutUsFooter;
            appointmentFooter.textContent = data[language].appointmentFooter;
            specialistsFooter.textContent = data[language].specialistsFooter;
            paymentFooter.textContent = data[language].paymentFooter;
            contactFooter.textContent = data[language].contactFooter;
            testimoniesFooter.textContent = data[language].testimoniesFooter;
            growyText.textContent = data[language].growyText;
            paymentLink.forEach(element => {
                element.textContent = data[language].stripeText;
            })
            paymentAnchor.forEach(element => 
                element.href = data[language].paymentLink
            )

            testimonyVideoOne.src = data[language].testimonyVideoOne;
            suggestionText.textContent = data[language].suggestionText;
            
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