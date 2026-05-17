minute = int(input(print("Enter a number of minutes: ")))


int day_sum = minutes / 1440
int minutes_remining = minutes % 1440
int year_sum = day_sum / 365
int days_remaining = day_sum % 365
int minute_left = minutes_remining / 60
                
print(year_sum +" years  "+ day_remaining +" days "+ minute_left + "minute\n")


  
