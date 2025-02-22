import smtplib
import os
from email.mime.text import MIMEText
from dotenv import load_dotenv
from flask import Flask, render_template, request

load_dotenv()
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/web/mail', methods=['GET', 'POST'])
def email():
    password = os.environ.get('MAIL_PASSWORD')
    print(password)
    if request.method == 'POST':
        subject = "Comentario en sitio web de Bencomo" 
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        msg = request.form["msg"]

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("javier.rod.dev@gmail.com", password )

        message  = MIMEText(f"subject: {subject}\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {msg}")

        message["from"] = "javier.rod.dev@gmail.com"
        message["to"] = "bencomodentalclinic@gmail.com"
        message["subject"] = subject

        server.sendmail("javier.rod.dev@gmail.com", "javier.rod.dev@gmail.com", message.as_string())

        server.quit()

        return render_template('home.html')

    else:
        return render_template('home.html')

@app.route('/web/mail/suggestions', methods=['GET', 'POST'])
def emailSuggestions():
    password = os.environ.get('MAIL_PASSWORD')
    if request.method == 'POST':
        subject = "Sugerencia en sitio web de Bencomo" 
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        msg = request.form["msg"]

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("javier.rod.dev@gmail.com", password )

        message  = MIMEText(f"subject: {subject}\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {msg}")

        message["from"] = "javier.rod.dev@gmail.com"
        message["to"] = "bencomodentalclinic@gmail.com"
        message["subject"] = subject

        server.sendmail("javier.rod.dev@gmail.com", "javier.rod.dev@gmail.com", message.as_string())

        server.quit()

        return render_template('home.html')

    else:
        return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
