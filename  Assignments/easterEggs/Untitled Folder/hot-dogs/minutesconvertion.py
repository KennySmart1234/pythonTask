minutes = int(input(print("Enter a number of minutes: ")))


day_sum = minutes / 1440
minutes_remining = minutes % 1440
year_sum = day_sum / 365
days_remaining = day_sum % 365
minute_left = minutes_remining / 60
                
print(year_sum, " years  ", days_remaining, " days ", minute_left, "minute\n")


  
