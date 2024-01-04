import getpass
import math

correct_username='lubna'
correct_password='li123'
balance=6000.0

while True:
    
    user_name=input("Enter the username please :")
    password=getpass.getpass("Enter your password :")
    
    if correct_username == user_name and correct_password == password:
        print("username and password are validated")
    
    else:
        print("please enter correct details:")    

    #user selection:
    print("")
    print("Banking basic operations:")
    print("Enter '1' for checking Balance:")
    print("Enter '2' for Transfering Funds:")
    print("Enter '3' for Depositing Money:")
    print("Enter '4' for Withdrawing Money:")
    print("Enter '5' for Viewing Balance Money:") 
    print("Enter '0' to Exit")
    choice=input("Enter your choice:")
     
    if choice == '1':
        print("{} your balance is :{}".format(user_name,float(balance)))
    elif choice == '2':
        reciepient=input("Enter the reciepient Account number: ")  
        tranfer_amount=float(input("Enter the amount to be tranfer:"))
        if balance > tranfer_amount:
            #reciepient += tranfer_amount
            current_balance=balance - tranfer_amount
            #reciepient += tranfer_amount
            #current_balance-=tranfer_amount
            
    
            print("Amount £{} transfered to '{}' account number,Successfully".format(tranfer_amount,reciepient))
            print("{} your current balance is : {}".format(user_name,float(current_balance)))
        else:
            print("Insufficient Amount: Sorry")    
            




