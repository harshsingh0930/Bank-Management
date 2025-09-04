# Bank Management
### Video Demo:  <https://youtu.be/bMQsPtjkEmk>
#### Description:
Bank management is a very simple project which ask users for new or existing account and if already an account exists with valid crn, It states your account is healthy(I could have added more functionality here specially balance check). If not valid CRN it exists the code if you say so. If new user it creates your account with some basic information like name, city, age, mobile and email. then for verfication it ask for email OTP and then email you your new CRN and store the data in csv file for future purpose.

#### main():
This function welcomes you and ask for new or existing user/customer. If existing and inputed crn is 4 digits it passes it to check_crn() else throw error. If a new user it pass it to create_new_user() . This function implements continuous operation through a while loop, ensuring users can perform multiple operations without restarting the program. Error handling is also there to manage invalid inputs.

#### create_new_user():
Ask name, age, city, mobile no, email for creating new user and then verify the email by verify_email() function and send the user their new crn to their email and stores the all the data in csv file. It also pass email and name and mobile number to other functions for desired input using regex.

#### check_crn():
It takes a input and check whether the given value is belongs to that specific heading or not which is CRN here in question. This function implements file reading operations.

#### send_crn():
It uses email.mime.text library to send email for OTP and CRN. This function uses Gmail's SMTP server to send emails, It send user their CRN directly to email to protect confeditional information.

#### get_name() and get_email():
Uses regex to get the desired input with a narrow escaping route. These functions implement robust input validation using regular expressions, ensuring data quality and consistency throughout the application. The regex patterns enforce specific formats for names and email addresses, preventing invalid data from entering the system.

## Design Decisions and Security Considerations

The project implements several security measures including email verification through OTP (One-Time Password) generation, secure CRN generation using random number generation, and input validation to prevent malicious data entry. The system advises users about security best practices, such as not sharing their CRN with others.

The choice to use a dedicated email account for the project demonstrates understanding of security principles while ensuring the application remains functional for demonstration purposes. This approach balances educational requirements with security consciousness.

## Learning Outcomes and Future Enhancements

This project successfully demonstrates proficiency in Python fundamentals including file I/O operations, regular expressions, email integration, random number generation, and modular programming design. The implementation showcases practical application development skills while maintaining code readability and functionality.

Future enhancements could include implementing balance management features, transaction history tracking, database integration for improved data handling, and web-based interface development to transform the console application into a full-featured web application.
