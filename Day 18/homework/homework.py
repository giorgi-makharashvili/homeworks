#2) პირობითი განცხადებები ჯერ უშვებენ პირველ პირობას და თუ True  იქნება გამოიტანს შედეგს, თუ False განაგრძობს შემდეგზე. ნაჩვენებია ნახაზზე.

#3)
num1 = int(input("enter num : "))
num2 = int(input("enter num : "))
if num1>num2:
     print(num1)
else:
     print(num2)

#4)
number = float(input("enter any number : ")) 
if number %2 == 0:
    print("even")
else:
    print("odd")

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

#9)
num1 = float(input("Enter number: "))
num2 = float(input("Enter number: "))
operator = input("Choose one operator: +, -, *, /, **, %  ")
if operator == "+":
    print(num1, "+", num2, "=", num1+num2)
elif operator == "-":
    print(num1, "-", num2, "=", num1-num2)
elif operator == "*":
    print(num1, "*", num2, "=", num1*num2)
elif operator == "/":
    if num2 == 0:
        print("გაყოფა 0-ზე არ შეიძლება")
    else:
        print(num1, "/", num2, "=", num1/num2)
elif operator == "**":
    print(num1, "**", num2, "=", num1**num2)
elif operator == "%":
    print(num1, "%", num2, "=", num1%num2)
else:
    print("Wrong operator")