history = open("history.txt", "w")
USER_BALANCE = 20000
s = 4594

pin=s

pin = int(input("Enter your pin? "))

if pin==s:
    print("Your current balance is: " + str(USER_BALANCE))
    while True:
        print("Press 1 To Withdraw ")
        print("Press 2 for Transaction  History ")
        print("Press 3 To Cancel ")
        answer = input("Enter your option ? ")

        if answer == "1":
           y = input("How much would you like to withdraw? ")

            #if float(y)<0:
                #print("Amount can not be less than 0")
           if float(y) <= USER_BALANCE:
                USER_BALANCE -= float(y)
                print("Your new balance is:" + str(USER_BALANCE))
                history.write("You withdraw an amount of " + y + "." + " " + "Current balance is " + str(USER_BALANCE) + "\n")
                continue



           else:
                    print("Cannot be done. You have insufficient funds.")



                #elif (answer == "ok" or answer == "OK"):
                    #pin = input("Enter pin: ")


        elif answer == "2":
            if history== "write":
                balancefile = open("history.txt", "r")
                print("Your Transaction History is: ")
                print(str(USER_BALANCE))
                #print("You Withdraw the amount: " + y)
                print(balancefile.read())
                balancefile.close()


            else:
                print("Transaction history is not found")


        elif answer == "3":
            pin=input("Enter pin: ")
        else:
                print("Please choose correct option")






else:
        print("Incorrect Pin")



