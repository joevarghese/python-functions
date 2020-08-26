def even(number):
    if (number % 2 == 0):
        return True
    else:
        return False      
def odd(number):
    if not even(number):
        print("The number is odd")
    else:
        print("The number is even")        
odd(24)
