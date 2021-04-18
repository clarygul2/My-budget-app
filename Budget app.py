budgetDict = [{"category": "food" "clothing" "entertainment", "all amount": 0}]

class Budget:
    
    def __init__(self):
        pass
    
    def deposit(self):
        print("Budget Options")
        print("1. Food")
        print("2. cloth")
        print("3. entertainment")
        selectedbudget = int(input("select your budget \n"))
        
        if selectedbudget == 1:
            print("FOOD BALANCE: ", budgetDict[0]["amount"])
            fd = int(input("do you want to deposit to food balance? 1(yes), 2(no) \n"))
            if fd == 1:
                deposit = int(input("Enter Amount\n"))
                deposit1 = budgetDict[0]["amount"] + deposit
                budgetDict[0]["amount"] = budgetDict[0]["amount"] + deposit
                print("NEW BALANCE: ",budgetDict[0]["amount"])
                op = int(input("do you want to  1(transfer), 2(withdraw), 3(quit)\n"))
                if op == 2:
                    self.withdrawfromBudget()
                    
                elif op == 1:
                    self.transfer()
                
                
            else:
                print("invalid Selection\nSELECT A VALID OPTION")
                self.deposit()
                
                
                
                                
        elif selectedbudget == 2:
            print("CLOTHING BALANCE: ",budgetDict[1]["amount"])
            fd = int(input("do you want to deposit to clothing balance? 1(yes), 2(no) \n"))
            if fd == 1:
                deposit = int(input("Enter Amount\n"))
                deposit1 = budgetDict[1]["amount"] + deposit
                budgetDict[1]["amount"] = budgetDict[1]["amount"] + deposit
                print("NEW BALANCE: ",budgetDict[1]["amount"])
                op = int(input("do you want to  1(transfer), 2(withdraw), 3(quit)\n"))
                if op == 2:
                    self.withdrawfromBudget()
                    
                elif op == 1:
                    self.transfer()
                
                
                else:
                    print("Have a Nice Day")
                    

            else:
                print("invalid Selection\nSELECT A VALID OPTION")
                self.deposit()
                
                
                
        elif selectedbudget == 3:
            print("CLOTHING BALANCE: ",budgetDict[2]["amount"])
            fd = int(input("do you want to deposit to clothing balance? 1(yes), 2(no) \n"))
            if fd == 1:
                deposit = int(input("Enter Amount\n"))
                deposit1 = budgetDict[2]["amount"] + deposit
                budgetDict[2]["amount"] = budgetDict[1]["amount"] + deposit
                print("NEW BALANCE: ",budgetDict[2]["amount"])
                op = int(input("do you want to  1(transfer), 2(withdraw), 3(quit)\n"))
                if op == 2:
                    self.withdrawfromBudget()
                    
                elif op == 1:
                    self.transfer()
                
                
                else:
                    print("Have a Nice Day")
                    

            else:
                print("invalid Selection\nSELECT A VALID OPTION")
                self.deposit()
                    

        else:
            print("Have a Nice Day")
                
                    
    def withdrawfromBudget(self):
        print(budgetDict)
        print("withdraw Options")
        print("1. Food")
        print("2. cloth")
        print("3. entertainment")
        selectedbudgetOption = int(input("select withdraw Options \n"))
        
        if selectedbudgetOption == 1:
            print("FOOD BALANCE: ",budgetDict[0]["amount"])
            withdraw = int(input("Enter Amount You Want To Withdraw\n"))
            if withdraw > budgetDict[0]["amount"]:
                print("Fnsuficent Funds")
                op = int(input("would you like to return home 1(yes), 2(no)"))
                if op == 1:
                    self.deposit()
                
            else:
                withdraw1 = budgetDict[0]["amount"] - withdraw
                budgetDict[0]["amount"] = budgetDict[0]["amount"] - withdraw
                print("Withdrawal Sucessful")
                print("FOOD NEW BALANCE: ",budgetDict[0]["amount"])
                op = int(input("would you like to return home 1(yes), 2(no)"))
                if op == 1:
                    self.deposit()
                
                
        elif selectedbudgetOption == 2:
            print("CLOTHING BALANCE: ",budgetDict[1]["amount"])
            withdraw = int(input("Enter Amount You Want To Withdraw\n"))
            if withdraw > budgetDict[1]["amount"]:
                print("Fnsuficent Funds")
                op = int(input("would you like to return home 1(yes), 2(no)"))
                if op == 1:
                    self.deposit()
                
            
            else:
                withdraw1 = budgetDict[1]["amount"] - withdraw
                budgetDict[1]["amount"] = budgetDict[1]["amount"] - withdraw
                print("Withdrawal Sucessful")
                print("CLOTHING NEW BALANCE: ",budgetDict[1]["amount"])
                op = int(input("would you like to return home 1(yes), 2(no)"))
                if op == 1:
                    self.deposit()
               
                
        elif selectedbudgetOption == 3:
            print("ENTERTAINMENT BALANCE: ",budgetDict[2]["amount"])
            withdraw = int(input("Enter Amount You Want To Withdraw\n"))
            if withdraw > budgetDict[2]["amount"]:
                print("Fnsuficent Funds")
                op = int(input("would you like to return home 1(yes), 2(no)"))
                if op == 1:
                    self.deposit()
                
            
            else:
                withdraw1 = budgetDict[2]["amount"] - withdraw
                budgetDict[2]["amount"] = budgetDict[2]["amount"] - withdraw
                print("Withdrawal Successful")
                print("ENTERTAINMENT NEW BALANCE: ",budgetDict[2]["amount"])
                op = int(input("would you like to return home 1(yes), 2(no)"))
                if op == 1:
                    self.deposit()
               
            
        else:
            print("invalid Selection\nSELECT A VALID OPTION")
            self.deposit()
            
            
            
    def transfer(self):
        print(budgetDict)
        print("Transfer Options")
        print("1.From  Food")
        print("2.From clothing")
        print("3.From entertainment")
        selectTransferoption = int(input("select destination\n"))
        
        if selectTransferoption == 1:
            print("FOOD BALANCE: ",budgetDict[0]["amount"])
            transfer = int(input("1.(Transfer to Clothing), 2.(Transfer to Entertainment)\n"))
            if transfer == 1:
                transferamount = int(input("Enter Amount\n"))
                if transferamount <= budgetDict[0]["amount"]:
                    transferamount1 = budgetDict[0]["amount"] - transferamount
                    transferamount2 = budgetDict[1]["amount"] + transferamount
                    budgetDict[0]["amount"] = budgetDict[0]["amount"] - transferamount
                    budgetDict[1]["amount"] = budgetDict[1]["amount"] + transferamount
                    transferamount2 = budgetDict[1]["amount"] + transferamount
                    print("TRANSFER SUCCESSFUL!!!")
                    print("NEW FOOD BALANCE: ",budgetDict[0]["amount"])
                    print("NEW CLOTHING BALANCE: ",budgetDict[1]["amount"])
                    ab = int(input("do you want to transfer again? 1(yes) 2(no)\n"))
                    if ab == 1:
                        self.transfer()
                    
                else:
                    print("insufficent funds")
                    print("FOOD BALANCE: ",budgetDict[0]["amount"])
                    self.deposit()
                    
            elif transfer ==2:
                transferamount = int(input("Enter Amount\n"))
                if transferamount <= budgetDict[0]["amount"]:
                    transferamount1 = budgetDict[0]["amount"] - transferamount
                    transferamount2 = budgetDict[2]["amount"] + transferamount
                    budgetDict[0]["amount"] = budgetDict[0]["amount"] - transferamount
                    budgetDict[2]["amount"] = budgetDict[2]["amount"] + transferamount
                    transferamount2 = budgetDict[1]["amount"] + transferamount
                    print("TRANSFER SUCCESSFUL!!!")
                    print("NEW FOOD BALANCE: ",budgetDict[0]["amount"])
                    print("NEW ENTERTAINMENT BALANCE: ",budgetDict[2]["amount"])
                    ab = int(input("do you want to transfer again? 1(yes) 2(no)\n"))
                    if ab == 1:
                        self.transfer()
                   
                    
                else:
                    print("insufficent funds")
                    print("FOOD BALANCE: ",budgetDict[0]["amount"])
                    self.deposit()
                    
        elif selecttransferoption ==2:
            print("CLOTHING BALANCE: ",budgetDict[1]["amount"])
            transfer = int(input("1.(Transfer to Entertainment), 2.(Transfer to Food)\n"))
            if transfer == 1:
                transferamount = int(input("Enter Amount\n"))
                if transferamount <= budgetDict[1]["amount"]:
                    transferamount1 = budgetDict[1]["amount"] - transferamount
                    transferamount2 = budgetDict[2]["amount"] + transferamount
                    budgetDict[1]["amount"] = budgetDict[1]["amount"] - transferamount
                    budgetDict[2]["amount"] = budgetDict[2]["amount"] + transferamount
                    transferamount2 = budgetDict[1]["amount"] + transferamount
                    print("TRANSFER SUCCESSFUL!!!")
                    print("NEW CLOTHING BALANCE: ",budgetDict[1]["amount"])
                    print("NEW ENTERTAINMENT BALANCE: ",budgetDict[2]["amount"])
                    aq = int(input("do you want to transfer again? 1(yes) 2(no)\n"))
                    if ab == 1:
                        self.transfer()
                        
                   
                else:
                    print("insufficent funds")
                    print("FOOD BALANCE: ",budgetDict[0]["amount"])
                    self.deposit()
                    
            elif transfer ==2:
                transferamount = int(input("Enter Amount\n"))
                if transferamount <= budgetDict[1]["amount"]:
                    transferamount1 = budgetDict[1]["amount"] - transferamount
                    transferamount2 = budgetDict[0]["amount"] + transferamount
                    budgetDict[1]["amount"] = budgetDict[1]["amount"] - transferamount
                    budgetDict[0]["amount"] = budgetDict[0]["amount"] + transferamount
                    transferamount2 = budgetDict[0]["amount"] + transferamount
                    print("TRANSFER SUCCESSFUL!!!")
                    print("NEW CLOTHING BALANCE: ",budgetDict[1]["amount"])
                    print("NEW FOOD BALANCE: ",budgetDict[0]["amount"])
                    ab = int(input("do you want to transfer again? 1(yes) 2(no)\n"))
                    if ab == 1:
                        self.transfer()
                    
                    
                else:
                    print("insufficent funds")
                    print("CLOTHING BALANCE: ",budgetDict[1]["amount"])
                    self.deposit()
                    
        elif selectTFoption ==3:
            print("ENTERTAINMENT BALANCE: ",budgetDict[2]["amount"])
            transfer = int(input("1.(Transfer to clothing), 2.(Transfer to Food)\n"))
            if transfer == 1:
                transferamount = int(input("Enter Amount\n"))
                if transferamount <= budgetDict[2]["amount"]:
                    transferamount1 = budgetDict[2]["amount"] - transferamount
                    transferamount2 = budgetDict[1]["amount"] + transferamount
                    budgetDict[2]["amount"] = budgetDict[2]["amount"] - transferamount
                    budgetDict[1]["amount"] = budgetDict[1]["amount"] + transferamount
                    transferamount2 = budgetDict[1]["amount"] + transferamount
                    print("TRANSFER SUCCESSFUL!!!")
                    print("NEW ENTERTAINMENT BALANCE: ",budgetDict[2]["amount"])
                    print("NEW CLOTHING BALANCE: ",budgetDict[1]["amount"])
                    ab = int(input("do you want to transfer again? 1(yes) 2(no)\n"))
                    if ab == 1:
                        self.transfer()
                   
                    
                else:
                    print("insufficent funds")
                    print("FOOD BALANCE: ",budgetDict[0]["amount"])
                    self.deposit()
                    
            elif transfer ==2:
                transferamount = int(input("Enter Amount\n"))
                if transferamount <= budgetDict[2]["amount"]:
                    transferamount1 = budgetDict[2]["amount"] - transferamount
                    transferamount2 = budgetDict[0]["amount"] + transferamount
                    budgetDict[2]["amount"] = budgetDict[2]["amount"] - transferamount
                    budgetDict[0]["amount"] = budgetDict[0]["amount"] + transferamount
                    transferamount2 = budgetDict[0]["amount"] + transferamount
                    print("TRANSFER SUCCESSFUL!!!")
                    print("NEW ENTERTAINMENT BALANCE: ",budgetDict[2]["amount"])
                    print("NEW FOOD BALANCE: ",budgetDict[0]["amount"])
                    ab = int(input("do you want to transfer again? 1(yes) 2(no)\n"))
                    if ab == 1:
                        self.transfer()
                   
                    
                else:
                    print("insufficent funds")
                    print("CLOTHING BALANCE: ",budgetDict[1]["amount"])
                    self.deposit()
                
            
        else:
            print("have a nice day!!!")
          
    
transaction = Budget()       
transaction.deposit()
    
