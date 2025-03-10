import smtplib
import os
import base64
import requests
from email.mime.text import MIMEText

from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/web/mail', methods=['GET', 'POST'])
def email():
    encoded_password = os.environ.get('MAIL_PASSSWORD')
    password = base64.b64decode(encoded_password).decode()

    TURNSTILE_SECRET_KEY = os.environ.get('TURNSTILE_SECRET_KEY', 'SECRET_KEY')

    if request.method == 'GET':
        return render_template('home.html')
    
    elif request.method == 'POST':
        turnstile_token = request.form.get('cf-turnstile-response', '')

    if verify_turnstile(turnstile_token, TURNSTILE_SECRET_KEY, request.remote_addr):
        return jsonify({'success': False, 'message': 'Error en la verificacion de seguridad'})
    

    subject = 'Comentario en sitio de Bencomo'
    name = request.form.get('name', '')
    email = request.form.get('email','')
    phone = request.form.get('phone', '')
    msg = request.form.get('msg', '')

    try: 
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('sitiowebbencomodentalclinic@gmail.com', password)

        security_info = f"\n\nInformacion de seguridad:\nIP: {request.remote_addr}\nUser-Agent: {request.headers.get('User-Agent', '')}"
        
        message_content = f"Nombre: {name}\nEmail: {email}\nTelefono: {phone}\nMensaje: {msg} {security_info}"
        message = MIMEText(message_content)

        message["FROM"] = "sitiowebbencomodentalclinic@gmail.com"
        message["To"] = "hralvarez@bencomodentalclinic.com"
        message["Subject"] = subject

        server.sendmail("sitiowebbencomodentalclinic@gmail.com", "hralvarez@bencomodentalclinic.com", message.as_string())
        server.quit()

        return render_template('home.html')
    
    except Exception as e:
        app.logger.error(f"Error Enviando email: {str(e)}")
        return jsonify({'success': False, 'message': 'Error al enviar el mensaje'})

def verify_turnstile(token, secret_key, remote_ip):
    if not token:
        return False
    
    data = {
        'secret': secret_key,
        'response': token,
        'remoteip': remote_ip
    }

    try: 
        response = requests.post('https://challenges.cloudflare.com/turnstile/v0/siteverify', data=data)
        result = response.json()
        return result.get('success', False)
    except Exception as e:
        app.logger.error(f"error verificando turnstile: {str(e)}")
        return False

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