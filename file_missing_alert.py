import paramiko
import smtplib
import datetime
import time
from email.message import EmailMessage
import os

# ========== CONFIGURATIONS ==========
REMOTE_HOST = "destination_server_ip"
REMOTE_PORT = 22
USERNAME = "ssh_username"
PASSWORD = "ssh_password"
REMOTE_PATH = "/path/"

SENDER_EMAIL = "@gmail.com"
RECEIVER_EMAIL = ["@gmail.com","@gmail.com"]
EMAIL_PASSWORD = ""   # Gmail App Password

# ========== TIME CHECK ==========
now = datetime.datetime.now()
allowed_start = now.replace(hour=1, minute=0, second=0, microsecond=0)
allowed_end = now.replace(hour=1, minute=30, second=0, microsecond=0)

if not allowed_start <= now <= allowed_end:
    print(f"Script run at {now.strftime('%H:%M:%S')} — outside allowed time window (01:00–01:30). Exiting.")
    exit()

# ========== GENERATE FILE PATTERN ==========
today_str = now.strftime("%Y%m%d")
expected_pattern = f"BIEDW_CRM_INFOFFERS_{today_str}_"

# Log file with date
today_log_name = f"mediation_check_{today_str}.log"

# ========== SSH TO REMOTE AND CHECK FILE ==========
def check_file():
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(REMOTE_HOST, port=REMOTE_PORT, username=USERNAME, password=PASSWORD)

        stdin, stdout, stderr = client.exec_command(f"ls -l {REMOTE_PATH} | grep '{expected_pattern}'")
        output = stdout.read().decode()
        error = stderr.read().decode()

        if error:
            return False, "SSH command error: " + error

        if expected_pattern not in output:
            return False, f"No file found with pattern {expected_pattern}*"

        # Look for file size
        for line in output.strip().split("\n"):
            parts = line.split()
            if len(parts) >= 5:
                size = int(parts[4])
                filename = parts[-1]
                if size == 0:
                    return False, f"File {filename} exists but size is 0 bytes."
                else:
                    return True, f"File {filename} found with size {size} bytes."

        return False, "File found but could not read size."

    except Exception as e:
        return False, f"Exception during SSH: {str(e)}"
    finally:
        client.close()

# ========== LOGGING FUNCTION ==========
def log_result(message):
    with open(today_log_name, 'a', encoding='utf-8') as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] {message}\n")

# ========== EMAIL ALERT ==========
def send_email_alert(subject, body, attachment=None):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = SENDER_EMAIL
    msg['To'] = ", ".join(RECEIVER_EMAIL) #join the list of receiver emails
    msg.set_content(body)

    # Optional HTML version
    msg.add_alternative(f"""
    <html>
      <body>
        <h2 style='color:black;'>Mediation File Alert</h2>
        <p>{body}</p>
      </body>
    </html>
    """, subtype='html')

    # If an attachment is provided, attach the log file
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

# ========== MAIN FLOW ==========
success, message = check_file()
log_result(message)
print(message)

if not success:
    send_email_alert("Mediation File Missing or Empty", message, today_log_name)
else:
    # If file is found and size is greater than 0, send success email
    success_message = f"File {expected_pattern} found and has a valid size."
    send_email_alert("Mediation File Successfully Received", success_message, today_log_name)
