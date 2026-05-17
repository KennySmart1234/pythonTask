def balance_calculation():
        
    deposit = 0
    withdraw = 0

    transction_amount = input("Enter your transactions details or done to stop: ")

    while transction_amount != "done":
        amount = int(transction_amount) 

        if amount < 0:
            withdraw = withdraw + amount
         

        else:
            deposit = deposit + amount
            
        transction_amount = input("Enter your transactions details or done to stop: ")
    return deposit + withdraw


final_account_balance = balance_calculation()

print("Final balance: ", final_account_balance)


    







