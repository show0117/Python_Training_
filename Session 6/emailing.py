import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd
content = MIMEMultipart()   #建立MIMEMultipart物件
text = '測試集資料'  #信件內容
fileToSend = 'mock_data.csv'  #附檔所在路徑
fp = open(fileToSend,encoding = 'big5')   #讀取要傳送的檔案
attachment = MIMEText(fp.read(), 'base64', 'utf-8')   #將讀取的檔案轉換成MIMEText格式
attachment.add_header("Content-Disposition", "attachment", filename= 'mock_data.csv') #指定檔名
fp.close()
content["subject"] = "課程資料"    #信件標題
part = MIMEText(text, _charset="UTF-8")   #將文字轉換成中文編碼
receivers = ['receiver1@gmail.com', 'receiver2@gmail.com']   #收件人(可多位)
sender = 'sender@gmail.com'   #寄件人
content["from"] =  sender #寄件者
content["to"] = ','.join(receivers)  #收件者
content.attach(part)  # 信件內容
content.attach(attachment)   #信件附檔
with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:
    smtp.ehlo()  # 驗證SMTP伺服器
    smtp.starttls()  # 建立加密傳輸
    smtp.login("my_gmail@gmail.com", "zmcbhlxxxxxxxxxx")  # 登入寄件者gmail
    smtp.send_message(content)  # 寄送郵件
    print("Complete!")