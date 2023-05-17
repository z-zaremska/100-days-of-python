import datetime as dt
import pandas as pd
import random
import smtplib

MY_EMAIL = 'name.surname@mail.com'
MY_EMAIL_PASSWORD = 'strong_paSSw0rd'
SMTP_SERVER = 'smtp.mail.com'

bd_data = pd.read_csv('birthdays.csv')
bd_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in bd_data.iterrows()}

today = (dt.date.today().day, dt.date.today().month)

if today in bd_dict:
    bday_person = bd_dict[today]
    letter_path = f'letter_templates/letter_{random.randint(1, 4)}.txt'

    with open(letter_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace('[NAME', bday_person.name.title())

    with smtplib.SMTP(SMTP_SERVER) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=bday_person.email,
            msg=f'Subject: Happy birthday!\n\n{contents}'
        )
