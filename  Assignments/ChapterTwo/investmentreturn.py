original_amount = 1000
annual_rate = 7/100
ten_years = 10
twenty_years = 20
thirty_years = 30


amount_ten = original_amount * (1 + annual_rate)**ten_years
amount_twenty = original_amount * (1 + annual_rate)**twenty_years
amount_thirty = original_amount * (1 + annual_rate)**thirty_years

print("amount for 10 years: ", amount_ten)
print("amount for 20 years: ", amount_twenty)
print("amount for 30 years: ", amount_thirty)

