


const stripe = Stripe('pk_test_51R9TpC08PmZA3EXpd1gRferweig1c8aXvAuMf93AzIMwFqdpz7mdnQkuW5DcfecYNUA5v0bXqyteIF7hqITyeDeO00d8CxcLCN');

initialize();
let checkout;

//Fetch
async function initialize() {
    const fetchClientSecret = () =>
        fetch("/create-checkout-session",{
            method: "POST",
            headers: { "Content-Type": "application/json" },
        })
            .then((r) => r.json())
            .then((r) => r.clientSecret);

        const appearance = {
            theme: 'stripe',
        }

    checkout = await stripe.initCheckout({
        fetchClientSecret,
        elementsOptions: { appearance },
    });

    const emailInput = document.getElementById("email");
    const emailErrors = document.getElementById("email-errors");

    //Collect the costumers email address
    emailInput.addEventListener("input", () => {
        //clean any validation errors
        emailErrors.textContent = "";
    });

    emailErrors.addEventListener("blur", async () => {
        const newEmail = emailInput.value;
        if(!newEmail){
            return;
        }
        const { isValid, message } = await validateEmail(newEmail);
        if(!isValid){
            emailErrors.textContent = message;
        }
    });

    //Create the payment Element
    const paymentElement = checkout.createPaymentElement();
    paymentElement.mount("#payment-element")

}

async function handleSubmit(e){
    e.preventDefault();
    setLoading(true);

    const email = document.getElementById("email").value;
    const { isValid, message } = await validateEmail(email);
    if (!isValid){
        showMessage(message);
        setLoading(false);
        return;
    }
    
    const { error } = await checkout.confirm();

    showMessage(error.message);

    setLoading(false);
}