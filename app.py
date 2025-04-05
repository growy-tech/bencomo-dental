import smtplib
import os
import base64
from email.mime.text import MIMEText
import requests
import stripe
from flask import Flask, render_template, request, jsonify, redirect, url_for
from stripe_products import get_stripe_products, get_product_per_id



app = Flask(__name__, static_url_path='',static_folder='static')

#Stripe Keys
stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')
stripe.api_version = '2025-03-31.basil'
DOMAIN = os.environ.get('DOMAIN')
#Subscriptions ids
SUBSCRIPTION_PRODUCTS = {
    "personal": "price_1R9FBA03Pt1W3mkVsLss3fwk",
    "family": "familyplan"
}

#turnstile cloudflare keys
TURNSTILE_SECRET_KEY = os.environ.get('TURNSTILE_SECRET_KEY')
TEST_KEY = '0x4AAAAAABAJmIdh1tZu0jIFrnMLQui9F3I'

# Main Route
@app.route('/')
def home():
    """Function thar return home page"""
    return render_template('home.html')

# Route to handle the mails send of the contact main form.
@app.route('/web/mail', methods=['GET', 'POST'])
def email():
    """Function that manages the form of coments
        in contact section
    """
    if request.method == 'POST':
        token = request.form.get('cf-turnstile-response')
        if not token:
            return "error Turnslite, token not found", 400
                
        payload = {
            'secret': TEST_KEY,
            'response': token,
            'remoteip': request.remote_addr
        }
        
        response = requests.post('https://challenges.cloudflare.com/turnstile/v0/siteverify', data=payload)
        result = response.json()

        if result.get('success'):
            encoded_password = os.environ.get('MAIL_PASSWORD')
            password = base64.b64decode(encoded_password).decode()
        
            subject = "Mensaje en sitio web de Bencomo" 
            name = request.form["name"]
            email = request.form["email"]
            phone = request.form["phone"]
            msg = request.form["msg"]

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login("sitiowebbencomodentalclinic@gmail.com", password )

            message  = MIMEText(f"subject: {subject}\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {msg}")

            message["from"] = "sitiowebbencomodentalclinic@gmail.com"
            message["to"] = "hralvarez@bencomodentalclinic.com"
            message["subject"] = subject

            server.sendmail("sitiowebbencomodentalclinic@gmail.com", "hralvarez@bencomodentalclinic.com", message.as_string())

            server.quit()

        return render_template('home.html')
    else:
        return "Error, turnstile failed"

#Route to handle the mail send of the suggestions form.
@app.route('/web/mail/suggestions', methods=['GET', 'POST'])
def email_suggestions():
    """Function that handles suggestions of contact Section"""
    encoded_password = os.environ.get('MAIL_PASSWORD')
    password = base64.b64decode(encoded_password).decode()
    if request.method == 'POST':
        subject = "Sugerencia en sitio web de Bencomo" 
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        msg = request.form["msg"]

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("sitiowebbencomodentalclinic@gmail.com", password )

        message  = MIMEText(f"subject: {subject}\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {msg}")

        message["from"] = "sitiowebbencomodentalclinic@gmail.com"
        message["to"] = "javier.rod.dev@gmail.com"
        message["subject"] = subject

        server.sendmail("sitiowebbencomodentalclinic@gmail.com", "javier.rod.dev@gmail.com", message.as_string())

        server.quit()

        return render_template('home.html')

    else:
        return render_template('home.html')


@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    subscription_type = request.form.get('subscription-type')
    
    if subscription_type not in SUBSCRIPTION_PRODUCTS:
        return jsonify(error="Tipo de subscripcion invalido"), 400

    price_id = SUBSCRIPTION_PRODUCTS[subscription_type]

    try:
        session = stripe.checkout.Session.create(
            ui_mode = 'custom',
            line_items=[
                {
                    'price': price_id,
                    'quantity': 1,
                },
            ],
            mode='subscription',
            return_url=DOMAIN + '/return.html?session_id={CHECKOUT_SESSION_ID}',
        )
    except Exception as e:
        return str(e)

    return jsonify(clientSecret=session.client_secret)


@app.route('/checkout/<subscription_type>')
def checkout(subscription_type):
    if subscription_type not in SUBSCRIPTION_PRODUCTS:
        return redirect(url_for('home'))
    
    return render_template('checkout.html',subscription_type=subscription_type, public_key="pk_test_51Qk9mP03Pt1W3mkVYNF4NQdt3SjinNdpMVo48OAC9PKa4cjVgnBm3yqGpcTcoYAVRjr74oyLYLFs3Fbi0f4Of0xq00BKLGsJso")

@app.route('/session-status', methods=['GET'])
def session_status():
    session = stripe.checkout.Session.retrieve(request.args.get('session_id'))
    
    return jsonify(status=session.status, customer_email=session.customer_details.email)








if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True, port=5500)