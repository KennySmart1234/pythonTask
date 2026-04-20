#tirered discount based on customer
#customer spending in the store
#the higer the purhase 
#the higer the discount offered
 

purchased_amount = int(input("Enter Purchased "))


if (purchased_amount == 1000 or purchased_amount <= 10000):
        discount_amount = (purchased_amount * 0.05)
        print("Discount: ", purchased_amount - discount_amount)
if (purchased_amount == 10000 or purchased_amount <= 50000):
        discount_amount = (purchased_amount * 0.1)
        print("Discount", purchased_amount - discount_amount)
if (purchased_amount >= 50000):
        discount_amount = (purchased_amount * 0.2)
        print("Discount = ", purchased_amount - discount_amount)














