// This is your test publishable API key.
const stripe = Stripe("pk_test_51Qk9mP03Pt1W3mkVYNF4NQdt3SjinNdpMVo48OAC9PKa4cjVgnBm3yqGpcTcoYAVRjr74oyLYLFs3Fbi0f4Of0xq00BKLGsJso");

let checkout;

document.addEventListener("DOMContentLoaded", async () => {
  const subscriptionType = document.getElementById("subscription-type").textContent;

  if (!subscriptionType) {
    console.error("subscriptionType is required");
    return;
  }

  try {
    // Initialize Stripe Checkout with subscriptionType
    await initialize(subscriptionType);
  } catch (error) {
    console.error("Error initializing Stripe Checkout:", error);
    showMessage("Error initializing payment. Please try again.");
  }
});

async function initialize(subscriptionType) {
  // Send subscriptionType to the server and fetch the clientSecret
  const fetchClientSecret = () =>
    fetch("/create-checkout-session", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ subscriptionType: subscriptionType }),
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then((data) => {
        if (!data.clientSecret) {
          throw new Error("clientSecret not returned from server");
        }
        return data.clientSecret;
      });

  const appearance = {
    theme: "stripe",
  };

  // Initialize Stripe Checkout
  checkout = await stripe.initCheckout({
    fetchClientSecret,
    elementsOptions: { appearance },
  });

  // Configure the payment button text
  const payText = document.getElementById("pay-text").textContent;
  const nowText = document.getElementById("now-text").textContent;
  document.querySelector("#button-text").textContent = `${payText} ${checkout.session().total.total.amount} ${nowText}`;

  // Create and mount the payment element
  const paymentElement = checkout.createPaymentElement();
  paymentElement.mount("#payment-element");

  // Wait for the payment element to be ready
  paymentElement.on("ready", () => {
    console.log("Stripe payment element is ready.");
    document.querySelectorAll(".hidden").forEach((el) => {
      el.classList.remove("hidden");
    });
  });

  // Handle errors in the payment element
  paymentElement.on("change", (event) => {
    const errorContainer = document.getElementById("payment-message");
    if (event.error) {
      errorContainer.textContent = event.error.message;
      errorContainer.classList.remove("hidden");
    } else {
      errorContainer.textContent = "";
      errorContainer.classList.add("hidden");
    }
  });

  // Configure email validation
  const emailInput = document.getElementById("email");
  const emailErrors = document.getElementById("email-errors");

  emailInput.addEventListener("input", () => {
    emailErrors.textContent = "";
  });

  emailInput.addEventListener("blur", async () => {
    const newEmail = emailInput.value;
    if (!newEmail) {
      return;
    }

    const { isValid, message } = await validateEmail(newEmail);
    if (!isValid) {
      emailErrors.textContent = message;
    }
  });
}

const validateEmail = async (email) => {
  const updateResult = await checkout.updateEmail(email);
  const isValid = updateResult.type !== "error";

  return { isValid, message: !isValid ? updateResult.error.message : null };
};

document.querySelector("#payment-form").addEventListener("submit", handleSubmit);

async function handleSubmit(e) {
  e.preventDefault();
  setLoading(true);

  const email = document.getElementById("email").value;
  const { isValid, message } = await validateEmail(email);
  if (!isValid) {
    showMessage(message);
    setLoading(false);
    return;
  }

  const { error } = await checkout.confirm();

  // Handle errors during payment confirmation
  if (error) {
    showMessage(error.message);
  }

  setLoading(false);
}

// ------- UI helpers -------

function showMessage(messageText) {
  const messageContainer = document.querySelector("#payment-message");

  messageContainer.classList.remove("hidden");
  messageContainer.textContent = messageText;

  setTimeout(function () {
    messageContainer.classList.add("hidden");
    messageContainer.textContent = "";
  }, 4000);
}

function setLoading(isLoading) {
  if (isLoading) {
    // Disable the button and show a spinner
    document.querySelector("#submit").disabled = true;
    document.querySelector("#spinner").classList.remove("hidden");
    document.querySelector("#button-text").classList.add("hidden");
  } else {
    document.querySelector("#submit").disabled = false;
    document.querySelector("#spinner").classList.add("hidden");
    document.querySelector("#button-text").classList.remove("hidden");
  }
}