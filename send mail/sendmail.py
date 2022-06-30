# import smtplib

# try:
#     smtp = smtplib.SMTP('smtp.gamil.com',587)
#     smtp.starttls()

#     # smtp.login("sender_email_id", "sender_email_id_password")
#     smtp.login("shashikant.py8@gmail.com", "Shashi@1999")

#     massage = "I am SHAHSHI KANT KUMAR"

#     # smtp.sendmail("sender_email_id", "receiver_email_id", massage)
#     smtp.sendmail("shashikant.py8@gmail.com", "shashikant.skk.2016@gmail.com", massage)
#     smtp.quit()
     
#     print("SUCCESFULLY SEND MAIL")

# except Exception as e:
#     print("Something went to")





from http import server
import smtplib
# server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
# server.login = ("shashikant.py8@gmail.com", "shashi@1999")
# server.sendmail("shashikantssm6@gmail.com", "shashikant.skk.2016@gmail.com", "Hello")
# server.quit()
sender_email = "shashikant.py8@gmail.com"
rec_email = "shashikantssm6@gmail.com"
password = input(str("Please enter your password:"))
massage = "Hello"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender_email, password)
print("Login Success")
server.sendmail(sender_email,rec_email, massage)
print("Email has been send to receiver", rec_email)

