
import smtplib 
from email.message import EmailMessage


email = EmailMessage()
email['from'] = 'Anonymous'
email['to'] = ','
email['subject'] = 'Your account has been hacked!'

email.set_content('https://youtu.be/dQw4w9WgXcQ')

with smtplib.SMTP(host='smtp.gmail.com',port = 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('username','pass'')
    smtp.send_message(email)
    print('All accounts Hacked')


