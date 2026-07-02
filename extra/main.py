import smtplib as smtp
import random
import  datetime as dt
my_email = "testfreakgame@gmail.com"
password = "lmdq oqbd lgrx qgll"
to_addr = "testfreakgame@yahoo.com"

now = dt.datetime.now()
with open("quotes.txt", mode="r", encoding="utf-8") as quotes:
    quote = quotes.readlines()
my_quote = random.choice(quote)
if now.weekday() == 3:
    connection = smtp.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,to_addrs=to_addr,msg=f"Subject:Cheer up!\n\n{my_quote.encode("utf-8")}")
    connection.close()