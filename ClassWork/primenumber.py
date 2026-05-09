
def prime_nummber(number):

    for num in range(2,(number//2)+1):              
            if number == 1:
                return True
                
            if(number % num == 0):
                return False 
           
    return True
number = int(input("Enter a number "))          
print(prime_nummber(number))



