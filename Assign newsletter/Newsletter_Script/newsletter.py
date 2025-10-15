# import smtplib
# from email.message import EmailMessage
# from email.utils import formataddr
# import re

# def send_innovation_newsletter(sender_email, sender_password, recipient_email, html_content):
#     """Sends an HTML email newsletter."""

#     # Clean the HTML content
#     # html_content = html_content.replace('\xa0', ' ')  # Replace non-breaking spaces
#     # html_content = re.sub(r'[^\x00-\x7F]+', ' ', html_content)  # Remove non-ASCII chars

#     msg = EmailMessage()

#     msg['From'] = formataddr(('Innovation Newsletter', sender_email))
#     msg['To'] = formataddr(('Recipient', recipient_email))
#     msg['Subject'] = "Innovation Insights Newsletter"
#     # Set content type and charset before adding content
#     msg.set_content("This is a HTML email.")
#     # msg.add_alternative(html_content.encode('ascii', 'ignore').decode('ascii'), subtype='html')
#     msg.add_alternative(html_content, subtype='html', charset='utf-8')
#     try:
#         # Connect to the SMTP server
#         server = smtplib.SMTP('smtp.gmail.com', 587)
#         server.starttls()
#         server.login(sender_email, sender_password)
#         print("Successfully connected to the SMTP server!")

#         # Send the email
#         server.send_message(msg)
#         print("Email sent successfully!")

#     except Exception as e:
#         print(f"Error sending email: {e}")

#     finally:
#         server.quit()

# # --- IMPORTANT: REPLACE WITH YOUR ACTUAL VALUES ---
# sender_email = r'mailoc121517@gmai.com'  # Replace with your Gmail address
# sender_password = r"nhyv hvzg txdk hmte"  # Replace with your App Password (NOT your regular password)
# recipient_email = r"sonle161290@gmail.com" # Keep this as your email

# # --- Get the HTML content from the file (or you could define it as a string in the code) ---
# with open(r"D:\Materials_Tech\newsletter.html",  encoding="utf-8") as f:
#     html_content = f.read()

# # --- Send the email ---
# send_innovation_newsletter(sender_email, sender_password, recipient_email, html_content)


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr

def send_innovation_newsletter(sender_email, sender_password, recipient_email, html_content):
    """Sends an HTML email newsletter."""
    
    # Tạo message
    msg = MIMEMultipart('alternative')
    msg['From'] = formataddr(('Innovation Newsletter', sender_email))
    msg['To'] = formataddr(('Recipient', recipient_email))
    msg['Subject'] = "Innovation Insights Newsletter"
    
    # Tạo phần HTML với encoding utf-8
    html_part = MIMEText(html_content, 'html', 'utf-8')
    msg.attach(html_part)

    try:
        # Kết nối SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        print("Successfully connected to the SMTP server!")

        # Gửi email
        server.send_message(msg)
        print("Email sent successfully!")

    except Exception as e:
        print(f"Error sending email: {e}")

    finally:
        server.quit()

# Thông tin email
sender_email = r'mailoc121517@gmail.com'
sender_password = r"qfyq igtg cyse etzd"
recipient_email = r"mailoc221810@gmail.com"

# Đọc nội dung HTML
with open(r"D:\Materials_Tech\v2_tech_newsletter.html", encoding="utf-8") as f:
    html_content = f.read()

# Gửi email
send_innovation_newsletter(sender_email, sender_password, recipient_email, html_content)