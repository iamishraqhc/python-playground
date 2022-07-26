import smtplib
myemail = "test@gmail.com"
password = "testpassword"

connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(user = myemail, password = password)

connection.sendmail(from_addr = my_email, 
                    to_addr = "recipients@gmail.com",
                    msg = "Hello")

connection.close()
