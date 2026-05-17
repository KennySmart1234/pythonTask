principal = float(input("Enter the principal amount: "))

interest_rate = float(input("Enter the yearly interest rate: "))

year_duration = float(input("Enter the duration in a years: "))



interest_rate = (interest_rate)/100
rate = (interest_rate/12)

month_duration = (year_duration * 12)


rate_one = rate * ((1 + rate)**month_duration)




rate_two = (((1 + rate)**month_duration) - 1)

monthly_payment = (principal * (rate_one / rate_two))

print("monthly payment = ", monthly_payment)









