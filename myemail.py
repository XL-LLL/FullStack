import smtplib
from email.utils import formataddr
from email.mime.text import MIMEText

msg = MIMEText('Hello World!')
msg['From'] = formataddr(['<NAME>', '<EMAIL>'])
msg['To'] = '<EMAIL>'
msg['Subject'] = '标题'

server = smtplib.SMTP_SSL('smtp.qq.com', 465)
server.login('<EMAIL>', '<PASSWORD>')
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()