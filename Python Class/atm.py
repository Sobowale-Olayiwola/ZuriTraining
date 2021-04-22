from datetime import datetime
from datetime import date
import random

customer_accounts = ["0565794259", "0499180635", "0860156167", "0352223573", "0446542774", "0245307761", "0912332528"]
first_name_of_users = ['Olayiwola', 'Samuel', 'Kehinde', 'Chinedu', 'Saheed', 'Khalid', 'Onifade']
users_password = ['1970', '2345', '1234', '3456', '2005', '2000', '1989']
balance = [500_000 , 50_000, 200_000, 1_000_000, 600_000, 20_000, 700_000 ]

def display_home_page():
    print('Welcome to the best and most secured Bank')

def create_account_number():
    account_number = "0"
    for x in range(9):
        digit = random.randint(0,9)
        account_digit = str(digit)
        account_number = account_number+account_digit
    if account_number not in customer_accounts:
        customer_accounts.append(account_number)
        print('Your bank account number is: ' +account_number)
    else:
        create_account_number()

def user_registration():
    name = input('Please type in your name: \n')
    actual_name = name.capitalize()
    first_name_of_users.append(actual_name)
    print(first_name_of_users)
    password = int (input('Please create a four digit password to secure your account \n'))
    users_password.append(password)
    create_account_number()
    print('You have successfully created an account with us. Thanks for trusting us')
    initial_deposit = int (input('Please deposit an amount into your account to activate it \n'))
    balance.append(initial_deposit)
    print('You have deposited ' +str(initial_deposit))

def user_activity():
    print('These are the available options:')
    print('1. Withdrawal')
    print('2. Cash Deposit')
    print('3. Complaint')

    selected_option = int( input('Please select an option: \n'))
    if( selected_option == 1 ):
        amount_to_withdraw = int(input( 'How much would you like to withdraw? \n'))
        if( amount_to_withdraw <= balance[user_id] ):
            balance[user_id] = balance[user_id] - amount_to_withdraw
            print('Take your cash')
        else:
            print('Insufficient Funds')
                    
    elif( selected_option == 2):
            amount_to_deposit = int(input('How much would you like to deposit? \n'))
            balance[user_id] = balance[user_id] + amount_to_deposit
            string_format_of_balance = str(balance[user_id])
            print('Account balance is ' + string_format_of_balance )

    elif( selected_option == 3):
        customer_complaint = input('What issue will you like to report? \n')
        print('Thank you for contacting us.')
    else:
        print('Not a valid option')
        user_activity()
    

def user_login():
    name = input('Please type in your First Name: \n')
    actual_name = name.capitalize()
    if (actual_name in first_name_of_users):
        user_id = first_name_of_users.index(actual_name)
        password = input('Please type in your password: \n')
        if (password == users_password[user_id]):
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            print('Logged in at ' + dt_string )
            user_activity()
        else:
            print('Type in the correct password')
    else:
        print('Please check your First Name or not a registered user \n')
        print('You can register with us by choosing: \n 1. Yes \n')
        print('You can exit by choosing: \n 2. No \n')
        
        selected_option = int (input('Please choose Yes or No: \n'))
        if (selected_option == 1):
            user_registration()
        elif (selected_option == 2 ):
           print('Please take your ATM card') 
        else:
            display_home_page()

display_home_page()
user_login()

        


