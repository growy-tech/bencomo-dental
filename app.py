import smtplib
import os
import base64
import requests
from email.mime.text import MIMEText
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

TURNSTILE_SECRET_KEY = os.environ.get('TURNSTILE_SECRET_KEY')
TEST_KEY = '0x4AAAAAABAJmIdh1tZu0jIFrnMLQui9F3I'


# Main Route
@app.route('/')
def home():
    return render_template('home.html')

# Ruta para manejar el envío de correos
@app.route('/web/mail', methods=['GET', 'POST'])
def email():
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
            message["to"] = "halvarez@bencomodentalclinic@gmail.com"
            message["subject"] = subject

            server.sendmail("sitiowebbencomodentalclinic@gmail.com", "halvarez@bencomodentalclinic@gmail.com", message.as_string())

            server.quit()

        return render_template('home.html')
    else:
        return "Error, turnstile failed"

@app.route('/web/mail/suggestions', methods=['GET', 'POST'])
def emailSuggestions():
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

if __name__ == '__main__':
    app.run(debug=True, port=5500)