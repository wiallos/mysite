from flask import Flask, send_file, render_template_string, request, redirect
import sqlite3
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


app = Flask(__name__)

@app.route('/')
def index():
    with open('index.html', 'r', encoding='utf-8') as file:
        html_content = file.read()
    return render_template_string(html_content)

# @app.route('/submit', methods=['POST'])
# def submit():
#     name = request.form['name']
#     phone = request.form['phone']
#     message = request.form['message']

#     # Сформируем сообщение
#     email_message = MIMEMultipart()
#     email_message['From'] = SMTP_USERNAME
#     email_message['To'] = RECIPIENT_EMAIL
#     email_message['Subject'] = 'Новое сообщение с сайта'
        
#     body = f'Имя: {name}\nТелефон: {phone}\nСообщение: {message}'
#     email_message.attach(MIMEText(body, 'plain'))

#         # Отправка сообщения через SMTP сервер
#     try:
#         server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
#         server.starttls()
#         server.login(SMTP_USERNAME, SMTP_PASSWORD)
#         server.sendmail(SMTP_USERNAME, RECIPIENT_EMAIL, email_message.as_string())
#         server.quit()
#         return redirect(url_for('index'))
#     except Exception as e:
#         return str(e)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    phone = request.form['phone']
    message = request.form['message']

    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('INSERT INTO messages (name, phone, message) VALUES (?, ?, ?)', (name, phone, message))
    conn.commit()
    conn.close()


    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)