import smtplib
import datetime
import os
from email.message import EmailMessage

# ========== CONFIGURATIONS ==========

LOCAL_PATH = ""  # Path 

SENDER_EMAIL = "@gmail.com"
RECEIVER_EMAIL = ["@gmail.com", "@gmail.com"]
EMAIL_PASSWORD = ""   # Gmail App Password

now = datetime.datetime.now()
allowed_start = now.replace(hour=22, minute=00, second=0, microsecond=0)  
allowed_end = now.replace(hour=23, minute=59, second=59, microsecond=0)   

if not allowed_start <= now <= allowed_end:
    print(f"Script run at {now.strftime('%H:%M:%S')} — outside allowed time window (16:30–17:00). Exiting.")
    exit()


today_str = now.strftime("%Y%m%d")
expected_pattern = f"FILENAME_{today_str}_*"

today_log_name = f"{today_str}.log"

def check_file():
    try:
        file_found = False
        for filename in os.listdir(LOCAL_PATH):
            if filename.startswith(expected_pattern):
                file_found = True
                file_path = os.path.join(LOCAL_PATH, filename)
                file_size = os.path.getsize(file_path)
                if file_size == 0:
                    return False, f"File {filename} exists but size is 0 bytes."
                else:
                    return True, f"File {filename} found with size {file_size} bytes."

        return False, f"No file found - {expected_pattern}"

    except Exception as e:
        return False, f"Exception during checking: {str(e)}"

#log
def log_result(message):
    with open(today_log_name, 'a', encoding='utf-8') as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] {message}\n")

#alert
def send_email_alert(subject, body, attachment=None):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = SENDER_EMAIL
    msg['To'] = ", ".join(RECEIVER_EMAIL) 
    msg.set_content(body)

    msg.add_alternative(f"""
    <html>
      <body>
        <h2 style='color:black;'>File Alert</h2>
        <p>{body}</p>
      </body>
    </html>
    """, subtype='html')

    if attachment:
        with open(attachment, 'rb') as f:
            file_data = f.read()
            file_name = os.path.basename(attachment)
            msg.add_attachment(file_data, maintype="application", subtype="octet-stream", filename=file_name)

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(SENDER_EMAIL, EMAIL_PASSWORD)
            smtp.send_message(msg)
            print("Email alert sent.")
    except Exception as e:
        print(f"Failed to send email: {e}")

success, message = check_file()
log_result(message)
print(message)

if not success:
    send_email_alert("File Missing or Empty", message, today_log_name)
else:
    # If file is found and size is greater than 0, send success email
    # success_message = f"File {expected_pattern} found and has a valid size."
    send_email_alert("File Successfully Received", message, today_log_name)
