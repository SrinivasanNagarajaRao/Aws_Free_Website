import json
import smtplib
import urllib.parse
from email.mime.text import MIMEText

username = ""
password = ""
from_address = ""

success_response = {
        'statusCode': 200,
        'body': 'Message Sent Successfully'
    }


def lambda_handler(event, context):
    data = dict(urllib.parse.parse_qsl(event['body']))
    to_address = ["srinisav.it@gmail.com"]
    server = smtplib.SMTP('email-smtp.ap-south-1.amazonaws.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(username, password)
    message = MIMEText(str(data['message']))
    message['Subject'] = 'Topic: ' + str(data['subject']) +' Mail From: '+ str(data['email'])
    # to_address = to_address.append(str(event['email']))
    print(context)
    server.sendmail(from_addr=from_address, to_addrs=to_address, msg=str(message))
    server.close()
    return success_response