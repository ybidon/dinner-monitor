from http.server import BaseHTTPRequestHandler
import socket
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import json
from datetime import datetime

DOMAIN = "dinner.gettrumpmemes.com"
EMAIL_TO = "bourouis.yassine@gmail.com"
EMAIL_FROM = os.getenv("EMAIL_FROM")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

def check_dns():
    try:
        ip = socket.gethostbyname(DOMAIN)
        return {"status": "active", "ip": ip}
    except socket.gaierror:
        return {"status": "inactive"}

def send_email(ip):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_FROM
    msg['To'] = EMAIL_TO
    msg['Subject'] = f"DNS Record Found for {DOMAIN}"

    body = f"""
    The subdomain {DOMAIN} is now active!
    
    IP Address: {ip}
    Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    """

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_FROM, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()
        return True
    except Exception as e:
        print(f"Failed to send email: {str(e)}")
        return False

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        result = check_dns()
        
        if result["status"] == "active":
            send_email(result["ip"])
            response = {
                "message": "DNS record found",
                "ip": result["ip"]
            }
        else:
            response = {
                "message": "No DNS record yet"
            }
            
        self.wfile.write(json.dumps(response).encode())
        return 