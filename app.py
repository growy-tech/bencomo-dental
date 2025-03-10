import smtplib
import os
import base64
import requests
from email.mime.text import MIMEText
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Ruta principal
@app.route('/')
def home():
    return render_template('home.html')

# Ruta para manejar el envío de correos
@app.route('/web/mail', methods=['GET', 'POST'])
def email():
    # Verifica si la solicitud es GET
    if request.method == 'GET':
        return render_template('home.html')

    # Obtén la contraseña codificada desde las variables de entorno
    encoded_password = os.environ.get('MAIL_PASSWORD')
    if not encoded_password:
        app.logger.error("La variable de entorno MAIL_PASSSWORD no está configurada")
        return jsonify({'success': False, 'message': 'Error de configuración del servidor 1'})

    try:
        # Decodifica la contraseña
        password = base64.b64decode(encoded_password).decode()
    except Exception as e:
        app.logger.error(f"Error decodificando la contraseña: {str(e)}")
        return jsonify({'success': False, 'message': 'Error de configuración del servidor 2'})

    # Obtén la clave secreta de Turnstile desde las variables de entorno
    TURNSTILE_SECRET_KEY = os.environ.get('TURNSTILE_SECRET_KEY')
    if not TURNSTILE_SECRET_KEY:
        app.logger.error("La clave secreta de Turnstile no está configurada")
        return jsonify({'success': False, 'message': 'Error de configuración del servidor 3'})

    # Obtén el token de Turnstile desde el formulario
    turnstile_token = request.form.get('cf-turnstile-response', '')
    if not turnstile_token:
        app.logger.error("No se recibió el token de Turnstile")
        return jsonify({'success': False, 'message': 'Error en la verificación de seguridad'})

    # Verifica el token de Turnstile
    if not verify_turnstile(turnstile_token, TURNSTILE_SECRET_KEY, request.remote_addr):
        app.logger.error("Error en la verificación de Turnstile")
        return jsonify({'success': False, 'message': 'Error en la verificación de seguridad'})

    # Obtén los datos del formulario
    name = request.form.get('name', '')
    email = request.form.get('email', '')
    phone = request.form.get('phone', '')
    msg = request.form.get('msg', '')

    # Construye el contenido del correo
    subject = 'Comentario en sitio de Bencomo'
    security_info = f"\n\nInformacion de seguridad:\nIP: {request.remote_addr}\nUser-Agent: {request.headers.get('User-Agent', '')}"
    message_content = f"Nombre: {name}\nEmail: {email}\nTelefono: {phone}\nMensaje: {msg} {security_info}"
    message = MIMEText(message_content)
    message["From"] = "sitiowebbencomodentalclinic@gmail.com"
    message["To"] = "hralvarez@bencomodentalclinic.com"
    message["Subject"] = subject

    # Intenta enviar el correo
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('sitiowebbencomodentalclinic@gmail.com', password)
        server.sendmail("sitiowebbencomodentalclinic@gmail.com", "hralvarez@bencomodentalclinic.com", message.as_string())
        server.quit()
        app.logger.info("Correo electrónico enviado correctamente")
        return jsonify({'success': True, 'message': 'Mensaje enviado correctamente'})
    except Exception as e:
        app.logger.error(f"Error enviando email: {str(e)}")
        return jsonify({'success': False, 'message': 'Error al enviar el mensaje'})

# Función para verificar el token de Turnstile
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
        response.raise_for_status()  # Lanza una excepción si la respuesta no es 200 OK
        result = response.json()
        app.logger.info(f"Respuesta de Turnstile: {result}")  # Log para depuración
        return result.get('success', False)
    except requests.exceptions.RequestException as e:
        app.logger.error(f"Error verificando Turnstile: {str(e)}")
        return False

# Inicia la aplicación Flask
if __name__ == '__main__':
    app.run(debug=True)

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