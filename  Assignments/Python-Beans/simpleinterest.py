

principal = input("Enter the principal value: ")
rate = input("Enter the rate percentage: ")
time = input("Enter the time: ")

principal = int(principal)
rate = int(rate)
time = int(time)

rate_persentage = rate / 100


si = ((principal * rate_persentage * time) / 100)
total_amount = (principal + si)

print("SI = ", si, "   Total Amount", total_amount)
 








