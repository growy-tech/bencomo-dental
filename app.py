import smtplib
import os
import base64
from email.mime.text import MIMEText
import requests
import stripe
from flask import Flask, render_template, request, jsonify, redirect



#Stripe Keys
stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')
stripe.api_version = '2025-03-31.basil'
DOMAIN = os.environ.get('DOMAIN')

app = Flask(__name__)



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

#Route to configurate stripe session and choose the price id
@app.route('/config', methods=['GET'])
def get_prices():
    return({
        'personalPlan': os.getenv('PERSONAL_PLAN_PRICE_ID'),
        'familyPlan': os.getenv('FAMILY_PLAN_PRICE_ID')
    })

@app.route('/checkout-session', methods=['GET'])
def get_checkout_session():
    id = request.args.get('sessionId')
    checkout_session = stripe.checkout.Session.retrieve(id)
    return jsonify(checkout_session)

#Route to create Stripe checkout-session
@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    price = 'price_1R9rpp03Pt1W3mkVII4NhU3W'
    URL_DOMAIN = os.getenv('DOMAIN')

    try:
        session = stripe.checkout.Session.create(
            mode='subscription',
            ui_mode= 'custom',
            return_url= URL_DOMAIN + '/return.html?session_id={CHECKOUT_SESSION_ID}',
            line_items=[{
                'price': price,
                'quantity': 1
            }],
        )
    except Exception as e:
        return jsonify({'ERROR': {'message': str(e)}}), 400
    
    return jsonify(clientSecret=session.client_secret)

@app.route('/session-status', methods=['GET'])
def session_status():
    session = stripe.checkout.Session.retrieve(request.args.get('session_id'))

    return jsonify(status=session.status, costumer_email=session.costumer_details.email)

@app.route('/checkout', methods=['GET'])
def checkout_page():
    return render_template('checkout.html')

@app.route('/return', methods=['GET'])
def return_page():
    return render_template('return.html')

@app.route('/success', methods=['GET'])
def success_page():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True, port=5500)