import smtplib as smtp
import datetime as dt
import random
import pandas as pd



# current date time
now = dt.datetime.now()
year = now.year
month_now = now.month
day_now = now.day
weekday = now.weekday()
date_of_birth = dt.datetime(year = 1991, month = 2, day = 11)
# print(weekday)

my_email = "zzq01991@gmail.com"
password = "tsavaienyxixycdl"

# ----------------------send motivation quote--------------------------#

# with open ("quotes.txt") as file:
#     quotes = file.readlines()

# L = []
# for i in quotes:
#     i.replace("\n","")
#     L.append(i)

# picked_quote = random.choice (L)
# #print(picked_quote)


# if weekday == 3:
#     with smtp.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(user = my_email, password = password)
#         connection.sendmail(from_addr = my_email, 
#                             to_addrs = "godspeedzara@gmail.com", 
#                             msg = f"Subject:Happy Thursday\n\n{picked_quote}.")


# -------------------------send birthday wishes-----------------------------#     
data = pd.read_csv("birthdays.csv")
df = pd.DataFrame(data)

date_check = df[(df["month"] == month_now) & (df["day"] == day_now)]
name_check = date_check["name"].to_list()
email_check = date_check["email"].to_list()
# print(name_check)
# print(email_check)
# # #print(name_check, "-", email_check)


if len(name_check) != 0:
    letter_list = ["letter_1.txt","letter_2.txt","letter_3.txt"]
    random_letter = random.choice(letter_list)
    # print(random_letter)
    #print(type(name_check[0]))

    with open(random_letter) as file:
        file_content = file.read()
        new_file_content = file_content.replace("[NAME]",name_check[0])
        #print(new_file_content)



    with smtp.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user = my_email, password = password)
        connection.sendmail(from_addr = my_email, 
                            to_addrs = email_check[0], 
                            msg = f"Subject:Happy Birthday!\n\n{new_file_content}.")
