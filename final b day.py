##################### Extra Hard Starting Project ######################
import pandas as pd
import smtplib as smtp
import datetime as dt
import random
import os
my_email = os.environ.get("my_email")
password = os.environ.get("password_b_day")
# 1. Update the birthdays.csv
df = pd.read_csv("birthdays.csv")
# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
b_guys = df[(df["month"]==now.month) & (df["day"]==now.day)]
no_b_days = b_guys.shape[0]
b_guys_names = b_guys["name"]
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
for i in range(no_b_days):
    if not b_guys.empty:
        random_num = random.randint(1,3)
        with open(file=f"letter_templates/letter_{random_num}.txt", mode="r", encoding="utf-8") as file:
            letter_templates = file.read()
        specific_b_guy_name = b_guys_names[0]
        letter_templates = letter_templates.replace("[NAME]", specific_b_guy_name)
    # 4. Send the letter generated in step 3 to that person's email address.
        specific_b_guy_mail = b_guys[b_guys["name"]==specific_b_guy_name]["email"][0]
        with smtp.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,to_addrs=specific_b_guy_mail,msg="Subject:Happy Birthday \n\n"+letter_templates)



