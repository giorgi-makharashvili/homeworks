def square_digits(num):
    num1 = ""
    
    for i in str(num):
        num1 += str(int(i)**2)
    
    return int(num1)