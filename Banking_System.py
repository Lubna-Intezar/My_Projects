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
        break
    
    else:
        print("please, Enter correct details:")    
while True:
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

            #current_balance=balance - tranfer_amount
            balance -= tranfer_amount
            print("Amount £{} transfered to '{}' account number,Successfully".format(tranfer_amount,reciepient))
            print("{} your current balance is : {}".format(user_name,float(balance)))
        else:
            print("Insufficient Amount: Sorry") 

    elif choice == '3':

        deposit=float(input("Enter the amount to deposite: ")) 
        if deposit > 0:
            
            #current_balance+= deposit
            balance+= deposit
            print("successfully money{} deposited:".format(deposit))
            #print("{} your current balance is {} ".format(user_name,current_balance))
            print("{} your current balance is {} ".format(user_name,balance))
        else:
            print("invalid input")

    elif  choice == '4':

        withdraw=float(input("Enter the amount to withdraw: "))
        if balance > withdraw:
            #current_balance -= withdraw
            balance -= withdraw
            print("{} your current balance is {}".format(user_name,balance) )
            #print("{} your current balance is {}".format(user_name,current_balance) )

    elif choice == '5':
        print("Viewing balance money is {}".format(balance))
        # print("Viewing balance money is {}".format(current_balance))
    elif choice == '0':
        print("Exit")
        break    





    


            




