balance=500
pin=int(input("Enter your ATM pin="))
if pin == 1234:
        print("Correct Pin")
        print("Account Balace",balance,"/-")
        x=input("Do you want to withdraw money=")
        if x=="Y" or x=="y" or x=="YES" or x=="Yes" or x=="yes" :
                amount=int(input("Enter the amount(multiple of 100)="))
                if( amount%100==0):
                    if(amount<=balance):
                        print("Collect your cash")
                        print("Remaining balance=",balance-amount)
                        print("Have a nice day!See you soon!")    
                    else:
                        print("Insuficient balance")  
                else:
                    print("Enter the amount which is multiple of 100=")  
        else:
            print("Have a nice day!See you soon!")        
else:
    print("Incorrect pin")            

