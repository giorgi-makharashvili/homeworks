#5)
num1 = float(input("Enter number: "))
if num1 > 0:
    print(num1, "is positive")
else:
     print(num1, "is negative")

#6)
num2 = float(input("Enter number: "))
if num2 %5 == 0:
     print(num2, "is divisible by five")
else:
     print(num2, "is not divisible by five")

#7)
for i in range(5):
    num3 = int(input("Enter number: "))
    if num3 %2 == 0:
        print(num3, "is even")
    else:
        print(num3, "is odd")

 #8)
correct_pas = "Goa best"
count = 0
user_password = input("Enter password: ")

while user_password != correct_pas:
    count += 1
    user_password = input("Enter password: ")
print("Correct password!")
print("You needed", count, "tries")