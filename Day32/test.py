# env
from dotenv import load_dotenv
import os
import smtplib

load_dotenv()

to_email = os.getenv("TO_EMAIL")
from_email = os.getenv("FROM_EMAIL")
app_password = os.getenv("APP")

def send_email(to_email, subject, message):
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            # connection.set_debuglevel(1) 
            connection.starttls()
            connection.login(user=from_email, password=app_password)
            connection.sendmail(
                from_addr=from_email,
                to_addrs=to_email,
                msg=f"Subject:{subject}\n\n{message}"
            )
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
    
send_email(to_email, "Test Email", "This is a test email sent from Python.")