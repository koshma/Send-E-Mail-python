import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

host = "smtp.gmail.com"
port = 587

try:

    username = password = ""
    with open("usr.txt", "r") as f:
        file = f.readlines()
        username = file[0].strip()
        password = file[1].strip()
        from_email = file[2].strip()

    with open("recipient.txt", "r") as f:
        rec = f.readlines()
        to_list = rec[0].strip()

    email_conn = smtplib.SMTP(host, port)
    email_conn.ehlo()
    email_conn.starttls()
    email_conn.login(username, password)

    the_msg = MIMEMultipart("alternative")
    the_msg["Subject"] = "Subject"
    the_msg["From"] = from_email
    the_msg["To"] = to_list

    plain_txt = "Testing The MSG"
    html_txt = """\
    <html>
    <head></head>
    <body>
        <p>E-Mail Body Text</p>
    </body>
    </html>
    """

    part_1 = MIMEText(plain_txt, 'plain')
    part_2 = MIMEText(html_txt, "html")

    the_msg.attach(part_1)
    the_msg.attach(part_2)
    email_conn.sendmail(from_email, to_list, the_msg.as_string())
    email_conn.quit()

except smtplib.SMTPException:
    print("Error Sending message")
print("Sent")