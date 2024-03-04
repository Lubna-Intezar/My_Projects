
import math

while True:

    try:
        #requesting for user choice:

        user_choice=input("Enter your choice:\n 1:Investment\n 2:Bond \n 3:quit\n ")
    
        if user_choice.lower() == 'investment':

               #Calculating Investement:

                print("INVESTMENT-To calculate the amount of interest you'll earn on your investment :")
                calculation=input("enter your option(simple/compound):\n")

                if calculation.lower() == 'simple':

                     #declare user input for simple interest:

                     print("you have selected simple interest.\n ")

                     principal_amount = float(input("Enter the principal amount: "))
                     interest_rate = float(input("Enter the rate of interest: "))
                     time_period = float(input("Enter the time period (in years): "))

                     # Calculate simple interest:
                     simple_interest = (principal_amount * (1+interest_rate * time_period))

                     #Print the result for simple interest:
                     print("Simple Interest:", simple_interest)

                     #Calculating Compund Interest:    

                elif calculation.lower() == 'compound':

                     print("you have selected compound interest.")   
                     principal_amount = float(input("Enter the principal amount: "))
                     interest_rate = float(input("Enter the rate of interest: "))
                     time_period = float(input("Enter the time period (in years): "))

                     #using compund interest formula: 
                     compound_interest=principal_amount * math.pow((1+interest_rate),time_period)
                     print("compound interest is:",compound_interest)     

                else: 
                   print("Invalid choice. Please enter either 'simple interest' or 'compound interest'.")  

        #Calculation for Bond        

        elif user_choice.lower() == 'bond':

               print("BOND-To calculate the amount you'll have to pay on home loan :\n")
               present_value=float(input("Enter the present value:"))
               interest_rate=float(input("Enter the interst rate"))
               time_period=float(input("Enter the time period in a (month)"))

               #calculate how much user need to repay:

               repayment=(interest_rate * present_value) / (1-(1+interest_rate)**(-time_period))
               print("the bond is :" ,repayment)  
       
        #user to quit operation

        elif user_choice.lower() == 'quit':

            print("Sorry  you  exit  now...")
            break


        else:
               print("Invalid choice. Please enter either 'investment' or 'bond'. or quit")


       
    except ValueError:

        print("invalid input(please enter correct values):")           



   

           


    
         
