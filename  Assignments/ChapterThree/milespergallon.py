

gallon_used = float(input("Enter the gallons used (-1 to end): "))
miles_driven = float(input("Enter the miles driven: "))


miles_overall = 0
gallon_overall = 0
while gallon_used != -1:
    print("The miles/gallon for this tank was ", miles_driven / gallon_used)
    gallon_overall = gallon_overall + gallon_used
    miles_overall = miles_overall + miles_driven
    gallon_used = float(input("Enter the gallons used (-1 to end): "))
    miles_driven = float(input("Enter the miles driven: "))

   
print("The overall average miles/gallon was: ", miles_overall / gallon_overall)




























