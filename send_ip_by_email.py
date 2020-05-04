import socket
import time
import smtplib
from urllib.request import urlopen
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def send_mail(smtp_server, username, password, sender, receivers, subject, ip_address):
    message = MIMEText(ip_address)
    message['From'] = _format_addr('FromRaspberryIp <{}>'.format(sender))
    message['To'] = _format_addr('ToRaspberryIp <{}>'.format(','.join(receivers)))
    message['Subject'] = Header(subject, 'utf-8').encode()
    try:
        smtp_obj = smtplib.SMTP()
        smtp_obj.connect(smtp_server, 25)
        smtp_obj.set_debuglevel(1)
        smtp_obj.login(username, password)
        smtp_obj.sendmail(sender, receivers, message.as_string())
        smtp_obj.quit()
        print('send: {}'.format(ip_address))
    except smtplib.SMTPException as e:
        print('send error: {}'.format(e))


def check_network():
    while True:
        try:
            result = urlopen('http://www.baidu.com').read()
            print('network is ready...')
            break
        except Exception as e:
            print('Exception: {}'.format(e))
            print('Network is not ready,Sleep 5s...')
            time.sleep(5)


def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('1.1.1.1', 80))
    ipaddr = s.getsockname()[0]
    s.close()
    return ipaddr


if __name__ == '__main__':
    check_network()
    ipaddr = get_ip_address()
    send_mail('smtp.126.com', '<email_from_address>', '<email_from_address_token>', '<email_from_address>',
              ['<email_to_address>'], 'IP Address of Raspberry PI', ipaddr)
