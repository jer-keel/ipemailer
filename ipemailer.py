import ipgetter
import json
import smtplib
from threading import Timer
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

email_config_filepath = "email_config.json"

def get_and_send_ip():
	config = json.load(open(email_config_filepath))
	current_ip = ipgetter.myip()

	# Create the messgae
	msg = MIMEMultipart()
	msg["From"] = config["from_addr"]
	msg["To"] = config["to_addr"]
	msg["Subject"] = "Server Restarted"
	body_text = "Server IP: " + current_ip
	body = MIMEText(body_text, "plain")
	msg.attach(body)

	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()
	server.login(config["from_addr"], config["from_pass"])
	text = msg.as_string()
	server.sendmail(config["from_addr"], config["to_addr"], text)
	server.quit()

t = Timer(30.0, get_and_send_ip)
t.start()