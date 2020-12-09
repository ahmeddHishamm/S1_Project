import smtplib
import ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"


class Report:

    def __init__(self, subject, content, sender, pw):
        self.sender_email = sender
        self.password = pw
        self.subject = subject
        self.body = content

    def send_email(self):
        receiver_email = ""  # Enter receiver address
        message = f"""\
        Subject: {self.subject}
        
        {self.body}."""

        try:
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(self.sender_email, self.password)
                server.sendmail(self.sender_email, receiver_email, message)
        except:
            pass
pass





































# import sendgrid
# import os
# from sendgrid.helpers.mail import *
#
# sg = sendgrid.SendGridAPIClient(api_key=)
# from_email = Email("")
# to_email = To("")
# subject = "Test1"
# content = Content("text/plain", "this is a test for the reporting module for S1_project")
# mail = Mail(from_email, to_email, subject, content)
# response = sg.client.mail.send.post(request_body=mail.get())
# print(response.status_code)
# print(response.body)
# print(response.headers)
