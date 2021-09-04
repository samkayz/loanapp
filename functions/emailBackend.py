import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from webs.models import EmailConfig
from django.shortcuts import get_object_or_404
from email import encoders
from email.mime.base import MIMEBase
import pathlib



class EmailBackEnd:
    def sendEmail(self, template, receiverEmail, emailSubject):
        try:
            data = get_object_or_404(EmailConfig, name='email')

            username = data.username
            sender_email = data.default_email
            receiver_email = receiverEmail
            password = data.password
            port = data.port
            host = data.host

            message = MIMEMultipart("alternative")
            message["Subject"] = emailSubject
            message["From"] = sender_email
            message["To"] = receiver_email

            # Create the plain-text and HTML version of your message

            # Turn these into plain/html MIMEText objects
            part2 = MIMEText(template, "html")

            # Add HTML/plain-text parts to MIMEMultipart message
            # The email client will try to render the last part first
            message.attach(part2)

            # Create secure connection with server and send email
            if data.is_tls == True:
                context = ssl.create_default_context()
                with smtplib.SMTP(host, port) as server:
                    server.login(username, password)
                    # server.starttls(context=context)
                    server.sendmail(
                        sender_email, receiver_email, message.as_string()
                    )
            else:
                context = ssl.create_default_context()
                with smtplib.SMTP_SSL(host, port) as server:
                    server.login(username, password)
                    # server.starttls(context=context)
                    server.sendmail(
                        sender_email, receiver_email, message.as_string()
                    )
            pass

        except Exception as e:
            print(e)



    def sendEmailWithFile(self, template, emailSubject, receiverEmail, pathToFile, docName):
        try:
            data = get_object_or_404(EmailConfig, name='email')
            sender_email = data.default_email
            username = data.username
            password = data.password
            port = data.port
            host = data.host

            # Create a multipart message and set headers
            message = MIMEMultipart()
            message["From"] = data.default_email
            message["To"] = receiverEmail
            message["Subject"] = emailSubject

            message.attach(MIMEText(template, "html"))

            # filename = './cv.pdf'  # In same directory as script

            # Open PDF file in binary mode
            with open(pathToFile, "rb") as attachment:
                # Add file as application/octet-stream
                # Email client can usually download this automatically as attachment
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())

            # Encode file in ASCII characters to send by email    
            encoders.encode_base64(part)
            file_extension = pathlib.Path(pathToFile).suffix
            # Add header as key/value pair to attachment part
            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {docName}{file_extension}",
            )

            # Add attachment to message and convert message to string
            message.attach(part)
            text = message.as_string()

            # Log in to server using secure context and send email
            # context = ssl.create_default_context()
            if data.is_tls == True:
                with smtplib.SMTP(host, port) as server:
                    server.login(username, password)
                    server.sendmail(sender_email, receiverEmail, text)
            else:
                with smtplib.SMTP_SSL(host, port) as server:
                    server.login(username, password)
                    server.sendmail(sender_email, receiverEmail, text)
            pass

        except Exception as e:
            print(e)
        