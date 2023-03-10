import smtplib
import pandas as pd
import datetime as dt
import random

FILE_NAME = ["letter_1.txt", "letter_3.txt", "letter_2.txt"]
MY_EMAIL = "SENDER_EMAIL@gmail.com"               #Add Sender's/Your's Email Address
PASSWORD = "SENDER_PASSWORD"                       #Add Sender's/Your's Password

# 1. Please Update the birthdays.csv as per Your Requirements
df = pd.read_csv("birthdays.csv")



# 2. Check if today matches a birthday in the birthdays.csv

today = dt.datetime.now()
today_date = today.day
today_month = today.month
for ind in df.index:
    if today_date == df['day'][ind] and today_month == df['month'][ind]:
        recivers_name = df['name'][ind]
        recivers_email = df['email'][ind]
        rand_letter = random.choice(FILE_NAME)
        with open(f"letter_templates/{rand_letter}", 'r') as letter:
            random_letter = letter.read()
            msg = random_letter.replace("[NAME]", recivers_name)
                
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user= MY_EMAIL, password= PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs= recivers_email, 
                                msg=f"Subject:Happy BirthDay !!!\n\n{msg}")
            connection.close()



