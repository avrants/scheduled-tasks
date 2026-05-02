import os
import smtplib
import random
import datetime
import pandas as pd

SEND_FROM_EMAIL = os.environ.get("SEND_FROM_EMAIL")
SEND_FROM_PASSWORD = os.environ.get("SEND_FROM_PASSWORD")

today = datetime.datetime.today()
df_birthdays = pd.read_csv('birthdays.csv')

# Function Send email
def send_birthday_wish(to_email, subject, body):
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=SEND_FROM_EMAIL, password=SEND_FROM_PASSWORD)
        connection.sendmail(
            from_addr=SEND_FROM_EMAIL,
            to_addrs=to_email,
            msg=f"Subject: {subject}\n\n{body}"
        )

# Function read rand letter
def read_random_letter():
    with open(f"letter_templates/letter_{random.randint(1, 3)}.txt", "r") as f:
        rand_letter = f.read()
    return rand_letter

# Check for birthdays today
for index, row in df_birthdays.iterrows():
    if row['month'] == today.month and row['day'] == today.day:
        letter = read_random_letter()
        message = letter.replace("[NAME]", row['name'])
        send_birthday_wish(to_email=row['email'], subject="Happy Birthday!", body=message)





