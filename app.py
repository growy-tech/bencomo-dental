import smtplib
import os
import base64
from email.mime.text import MIMEText

from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/web/mail', methods=['GET', 'POST'])
def email():
    encoded_password = os.environ.get('MAIL_PASSWORD')
    password = base64.b64decode(encoded_password).decode()
    SECRET_KEY = "6Le4MvAqAAAAAEoI6ulWVwY9Yet6Lpjoy2gS9nWu"

    if request.method == 'POST':
        respuesta_recaptcha = request.form.get('g-recaptcha-reponse')
        subject = "Comentario en sitio web de Bencomo" 
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        msg = request.form["msg"]

        if not respuesta_recaptcha:
            return jsonify  ({'success': False, 'message': 'Por favor, complete el Captcha'})
        
        datos = {
            'secret': SECRET_KEY,
            'response': respuesta_recaptcha
        }

        respuesta = request.post('https://www.google.com/recaptcha/api/siteverify', data=datos)
        resultado = respuesta.json()

        if resultado['sucess']:
            subject = "Comentario en sitio web de Bencomo" 
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
    app.run(debug=False)
