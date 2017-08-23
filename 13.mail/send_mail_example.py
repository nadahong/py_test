import smtplib
from email.message import EmailMessage


msg = EmailMessage()
msg['Subject'] = '제목'
msg['From'] = ''
msg['To'] = 'soongon@hucloud.co.kr, ssgoni@naver.com'
msg.set_content('''
안녕하세요.

보내주신 메일 잘 확인했습니다.
좋은하루 되세요.
''')


smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
smtp.ehlo()
# smtp.starttls()
smtp.login('soongon@gmail.com', 'tnsrhsl33')
smtp.send_message(msg)
smtp.quit()

