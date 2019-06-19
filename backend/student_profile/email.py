import smtplib, ssl

def send_mail(url,mailid):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "prakhark19@gmail.com"  # Enter your address
    receiver_email = mailid # Enter receiver address
    password = "gogogreen"
    message = """\
    Subject: Hi there

    This message is the line http://127.0.0.1:8000/students/upload/{}/{}.""".format(url,mailid.split("@")[0])

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)