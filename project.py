import csv
import re
import random
import sys
import smtplib
from email.mime.text import MIMEText

def main():
    while True:
        get = input("Welcome to Gakuin Bank of Ohio \nNew or existing customer? ").strip().lower()
        if get == "existing":
            while True:
                crn = input("Enter your 4 digit CRN: ").strip()
                if len(crn) != 4 or not crn.isdigit():
                    print("Invalid length or not digits")
                else:
                    if check_crn(crn):  break
                    else:
                        ans = input("Want to enter re-enter CRN or check another CRN? y/n ")
                        if ans != "y":
                            sys.exit("Thank you for your time ")
        elif get == "new":
            crn = create_new_user()
            return crn
        else:
            print("Sorry.... what?")

crn = None
email = None
def create_new_user():
    global crn, email
    print("Thank you for giving us a chance, Complete the following details to get started.")
    name = get_name()
    age = input("Current age: ")
    city = input("City: ")
    mobile_num = get_num()
    crn = random.randint(1000,9999)
    email = get_email()
    verify_email(email)
    with open("bank_data.csv", "a") as file:
        data = csv.DictWriter(file, fieldnames=["Name", "Age", "City", "Mobile Number", "Email", "CRN"], lineterminator="\n")
        data.writerow({"Name": name, "Age": age, "City": city, "Mobile Number": mobile_num, "Email": email, "CRN": crn})
    print("Thanks for Verification. Your CRN is sent to your registered Email address\
          ")
    send_crn(crn)
    return crn

def check_crn(x):
    with open("bank_data.csv", "r") as file:
        read = csv.DictReader(file)
        for i in read:
            if i["CRN"] == x:
                print("Your account is healthy")
                return True
        print("Crn not found")
        return False


def send_crn(x):
    global email
    msg = MIMEText(f"Hello user your CRN is {x}. Do not share your CRN with anyone. We never ask for your CRN.")
    msg['Subject'] = 'Gakuin Bank of Ohio - Verification code'
    msg['From'] = sender_email
    msg['To'] = email

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, app_password)
    server.send_message(msg)
    server.quit()
sender_email = "example@domain.com"
app_password = "abcd efgh ijkl mnop"


def get_name():
    while True:
        name = input("Enter full name(Title is must): ").strip().title()
        if re.match(r"^[A-Za-z]+( [A-Za-z]+)? [A-Za-z]+$",name):
            return name
        else:
            print("Name is not satifying the conditions")

def get_num():
    while True:
        mob = input("Mobile Number: ").strip()
        if re.match(r"^[0-9]{10}$",mob):
            return mob
        else:
            print("Enter correct 10 digit mobile number")

def get_email():
    while True:
        email = input("Enter your email address: ").strip()
        if re.match(r"^\w+(\.\w+)?@\w+\.\w+(\.\w+)?$",email):
            return email
        else:
            print("Enter a valid email address")


def verify_email(user_email):
    global crn
    otp = random.randint(10000, 99999)
    msg = MIMEText(f"Hello user, OTP for validating the creation of new account is {otp}. Do not share the OTP with others, In case not requested by you kindly ignore it. ")
    msg['Subject'] = 'Gakuin Bank of Ohio - Verification code'
    msg['From'] = sender_email
    msg['To'] = user_email

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, app_password)
        server.send_message(msg)
        server.quit()
        while True:
            user_otp = input("Enter email OTP: ")
            if user_otp == str(otp):
                print("Email Verified")
                return True
            else:
                print("Incorrect OTP")
    except Exception as e:
        print(f"Error: {e}")
        return None

sender_email = "anything@domain.com"   # Use you testing mail id here
app_password = "cdfg fhhg hysg sasj"   # Create app passowrd, like for gmail follow this [guide](https://support.google.com/mail/answer/185833?hl=en)

def get_crn():
    crn = random.randint(1000,9999)
    return crn

if __name__ == "__main__":
    main()
