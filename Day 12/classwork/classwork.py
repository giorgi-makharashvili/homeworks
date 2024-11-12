#1)
print(True or True)#true
print(True or False)#true
print(False or True)#true
print(False or False)#false

print(True and True)#true
print(True and False)#false
print(False and True)#false
print(False and False)#false

#2)
num = int(input("enter your number: "))
num1 = int(input("enter your 2nd number: "))
print(num > 30 and num1 < 40)
print(num > 100 or num1 < 50)