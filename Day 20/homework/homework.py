#2) elif ს ვიყენებთ როდესაც if ში გვაქვს ორზე მეტი შესაძლო ვარიანტი და elif ით შეგვიძლია რამედენიც გვინდა იმდენი დავამატოთ.

#3)
num = int(input("enter your number: "))
num1 = int(input("enter your number: "))
num2 = int(input("enter your number: "))
if num > num1 and num > num2:
    print(num, "is the largest")
elif num1 > num and num1 > num2:
    print(num1, "is the largest")
else:
    print(num2, "is the largest")

#4)
num3 = int(input("enter your score 0_100: "))
if num3 >= 90 and num3 <= 100:
    print("your grade is: A")
elif num3 >= 80 and num3 <= 89:
    print("your grade is: B")
elif num3 >= 70 and num3 <= 79:
    print("your grade is: C")
elif num3 >= 60 and num3 <= 69:
    print("your grade is: D")
elif num3 < 60:
    print("your grade is: F")
else:
    print("your score is not valid.")

#5)
num4 = float(input("Enter number: "))
if num4 > 0:
    print(num1, "is positive")
elif num4 < 0:
    print(num1, "is negative")
else:
    print("is 0")

#6)

