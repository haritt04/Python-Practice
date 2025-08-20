import smtplib
from email.message import EmailMessage

#Email Configuration
sender_email = ""
receiver_email = ""
app_password = ""  # Replace this with your Gmail App Password

#Create the Email
msg = EmailMessage()
msg['Subject'] = 'Alert: File Missing in Mediation'
msg['From'] = sender_email
msg['To'] = receiver_email

#Plain text version
msg.set_content('No file was received in the last 30 minutes. Please investigate.')

#HTML version
msg.add_alternative("""\
<html>
  <body>
    <h2 style="color:red;">Alert: File Missing!</h2>
    <p>No files were received in the mediation folder at <strong>10:30 PM</strong>.</p>
    <p>Please check your system logs for more information.</p>
  </body>
</html>
""", subtype='html')

#Attach Log File (if it exists)
log_filename = "log.txt"
try:
    with open(log_filename, "rb") as file:
        file_data = file.read()
        file_name = file.name
        msg.add_attachment(file_data, maintype="application", subtype="octet-stream", filename=file_name)
        print(f"📎 Attached log file: {file_name}")
except FileNotFoundError:
    print(f"Log file '{log_filename}' not found — continuing without attachment.")

#Send the Email
try:
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(sender_email, app_password)
        smtp.send_message(msg)
        print("Alert email sent successfully!")

except smtplib.SMTPAuthenticationError:
    print("Authentication failed. Please check your email and app password.")
except Exception as e:
    print(f"Failed to send email: {e}")
