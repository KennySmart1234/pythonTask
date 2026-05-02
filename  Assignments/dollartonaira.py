def dollar_to_naira(dollar_amount, exchange_rate = 1550):
    

    if dollar_amount <= 0:
        ("Enter higher amount: ")
        return None

    naira_amount = dollar_amount * exchange_rate
    return naira_amount
    

dollar_amount = int(input("Enter dollar amount: "))
conversion_result = dollar_to_naira(dollar_amount)
print("Your naira amount is: ", conversion_result)







