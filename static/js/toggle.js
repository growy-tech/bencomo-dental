document.addEventListener('DOMContentLoaded', () =>  {
    const arrowHours = document.getElementById('hours');
    const hoursDiv = document.getElementById('hours-div');
    const ubication = document.getElementById('ubication');
    const ubicationDiv = document.getElementById('ubication-div')
    const arrowOfHours = document.getElementById('arrow-hours')
    const arrowOfUbication = document.getElementById('arrow-ubication')
    const pay = document.getElementById('pay')
    const payDiv = document.getElementById('pay-div')
    const arrowOfPay = document.getElementById('arrow-pay')

    arrowHours.addEventListener('click', () => {
        hoursDiv.classList.toggle('hidden');
        arrowOfHours.classList.toggle('rotate-90')
    });
    ubication.addEventListener('click', () => {
        ubicationDiv.classList.toggle('hidden')
        arrowOfUbication.classList.toggle('rotate-90')
    })
    pay.addEventListener('click', () => {
        payDiv.classList.toggle('hidden')
        arrowOfPay.classList.toggle('rotate-90')
    })


})