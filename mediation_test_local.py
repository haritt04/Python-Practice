import smtplib
from email.message import EmailMessage
import datetime
import os

# ======= CONFIGURATIONS =======
SENDER_EMAIL = "@gmail.com"  # Replace with your email
EMAIL_PASSWORD = ""   # Use Gmail App Password
RECEIVER_EMAILS = [
    "@gmail.com",
    "]@gmail.com"
]

today = datetime.datetime.now()
today_str = today.strftime("%Y%m%d")
log_filename = f"{today_str}.log"

def log_result(message):
    with open(log_filename, 'a', encoding='utf-8') as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] {message}\n")


# ======= EMAIL ALERT FUNCTION =======
def send_email_alert(subject, body, attachment=None):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = SENDER_EMAIL
    msg['To'] = ", ".join(RECEIVER_EMAILS)
    msg.set_content(body)

    msg.add_alternative(f"""
    <html>
      <body>
        <h2 style='color:black;'>File Alert</h2>
        <p>{body}</p>
      </body>
    </html>
    """, subtype='html')

    if attachment and os.path.exists(attachment):
        with open(attachment, 'rb') as f:
            file_data = f.read()
            file_name = os.path.basename(attachment)
            msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login(SENDER_EMAIL, EMAIL_PASSWORD)
            smtp.send_message(msg)
            print("Email alert sent.")
    except Exception as e:
        print(f"Failed to send email: {e}")

simulate_success = False  # Set to True to simulate a success scenario

if simulate_success: 
    result_message = "File found and size is valid."
    subject = "File Successfully Received."
else:
    result_message = "File missing or empty."
    subject = "File Missing or Empty."

log_result(result_message)
print(result_message)
send_email_alert(subject, result_message, log_filename)
