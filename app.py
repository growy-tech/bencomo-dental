import smtplib
# from flask_cors import CORS
import os
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart 
import requests
import stripe
from flask import Flask, render_template, request, jsonify, redirect, make_response, url_for
import stripe.error



app = Flask(__name__, static_url_path='',static_folder='static')
# CORS(app)

#Stripe Keys
stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')
stripe.api_version = '2025-03-31.basil'

DOMAIN = os.environ.get('DOMAIN')
#Subscriptions ids
SUBSCRIPTION_PRODUCTS = {
    "personalMx": "price_1RCMzQ03Pt1W3mkVEty6xkE7",
    "familyMx": "price_1RCN0003Pt1W3mkVJlRXb929",
    "personalUs": "price_1RCN1m03Pt1W3mkV6uGXfrCK",
    "familyUs": "price_1RCN2T03Pt1W3mkV1n20fVzi"
}
# price_id = 'price_1RCMzQ03Pt1W3mkVEty6xkE7'

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

@app.route('/check-subscription-type', methods=['POST'])
def check_subscription_type():
    try:
        data = request.get_json()
        subscription_type = data.get('textValue')
        price_id = SUBSCRIPTION_PRODUCTS[subscription_type]
        response = jsonify({'price_id': price_id})
        response.set_cookie('price_id', price_id)
        print(subscription_type)
        print(price_id)

        return response
    except Exception as e:
        return e

#Decorator for handle cache
def no_cache(view):
    def no_cache_wrapper(*args, **kwargs):
        response = make_response(view(*args, **kwargs))
        response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
        response.headers["Pragma"] = "no-cache"
        response.headers["Expires"] = "0"
        return response
    return no_cache_wrapper
        

@app.route('/create-checkout-session', methods=['POST'], endpoint='create_checkout_session')
@no_cache
def create_checkout_session():
    try:
        #price_id = None
        price_id = request.cookies.get('price_id')
        # Crea la sesión de Stripe
        session = stripe.checkout.Session.create(
            ui_mode='custom',
            line_items=[
                {
                    'price': price_id,
                    'quantity': 1,
                },
            ],
            mode='subscription',
            return_url=url_for('success', _external=True) + '?session_id={CHECKOUT_SESSION_ID}',
        )

        # Devuelve el clientSecret
        return jsonify(clientSecret=session.client_secret)

    except Exception as e:
        # Maneja errores y devuelve un mensaje claro
        print("Error en create-checkout-session:", str(e))  # Depuración
        return jsonify(error=str(e)), 500


@app.route('/checkout/<subscription_type>', endpoint='checkout')
@no_cache
def checkout(subscription_type):
    if subscription_type not in SUBSCRIPTION_PRODUCTS:
        return redirect(url_for('home'))
    
    return render_template('checkout.html',subscription_type=subscription_type, public_key="pk_test_51Qk9mP03Pt1W3mkVYNF4NQdt3SjinNdpMVo48OAC9PKa4cjVgnBm3yqGpcTcoYAVRjr74oyLYLFs3Fbi0f4Of0xq00BKLGsJso")

@app.route('/session-status', methods=['GET'], endpoint='session_status')
@no_cache
def session_status():
    session = stripe.checkout.Session.retrieve(request.args.get('session_id'))
    
    return jsonify(status=session.status, customer_email=session.customer_details.email)

#send mail webhook
@app.route('/webhook', methods=['POST'])
def stripe_webhook():
    payload = request.get_data(as_text=True)
    sig_header = request.headers.get('Stripe-Signature')
    endpoint_secret = os.environ.get('STRIPE_WEBHOOK_SECRET')

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        print('invalid payload')
        return jsonify(success=False), 400
    except stripe.error.SignatureVerificationError as e:
        print('Invalid signature')
        return jsonify(success=False), 400
    
    #handle checkout.session.completed
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']

        #get the customer email
        customer_email = session.get('customer_details',{}).get('email')
        subscription_id = session.get('subscription')
        amount = session.get('amount_total')
        print(amount)

        subject = None
        mail_template = "mail.html"
        if amount == 239900:
            subscription_id = subscription_id
            subject = "Bienvenido a Bencomo Dental Plus"
            mail_template = "mail_family_mx.html"
        elif amount == 149900: 
            subscription_id = subscription_id
            subject = "Bienvenido a Bencomo Dental Plus"
            mail_template = "mail_personal_mx.html"
        elif amount  == 9900:
            subscription_id = subscription_id
            subject = "Welcome to your membership"
            mail_template = "mail_personal_us.html"
        elif amount == 19900:
            subscription_id = subscription_id
            subject = "Welcome to your membership"
            mail_template = "mail_family_us.html"
        else:
            message_body = f"Bienvenido a tu plan Bencomo Dental Plus {subscription_id}"
            subject = "Welcome to your membership | Bienvenido a tu membresia"
        
        if customer_email:
            send_confirmation_email(customer_email, subscription_id, subject, mail_template)

    return jsonify(success=True), 200

def send_confirmation_email(customer_email, subscription_id, subject, template_name):
    try:
        # Decodifica la contraseña del correo
        encoded_password_memberships = os.environ.get('MAIL_MEMBERSHIPS_PASSWORD')
        password = base64.b64decode(encoded_password_memberships).decode()

        # Carga el archivo HTML correspondiente como plantilla
        template_path = f"templates/{template_name}"
        with open(template_path, "r") as file:
            html_template = file.read()

        # Reemplaza los valores dinámicos en la plantilla
        html_content = html_template.format(
            subscription_id=subscription_id,
            subject=subject, customer_email=customer_email
        )

        # Configura el servidor SMTP
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("membresias@bencomodentalclinic.com", password)

        # Crea el mensaje de correo
        message = MIMEMultipart("alternative")
        message["from"] = "membresias@bencomodentalclinic.com"
        message["to"] = customer_email
        message["subject"] = subject

        # Adjunta el contenido HTML al correo
        message.attach(MIMEText(html_content, "html"))

        # Envía el correo
        server.sendmail("membresias@bencomodentalclinic.com", customer_email, message.as_string())
        server.quit()

        print(f"Correo enviado a {customer_email}")
    except Exception as e:
        print(f"Error al enviar el correo {str(e)}")

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/cancel')
def cancel():
    return render_template('cancel.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True, port=5500)