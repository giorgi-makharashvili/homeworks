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
num6 = int(input("enter your 1 number: "))
num7 = int(input("enter your 2 number: "))
g = 0
for i in range(num6,num7+1):
    g+=i
print(g)
#7)
num8 = int(input("Enter your number: "))
is_valid = True

if num8 < 0:
    is_valid = False
for i in range(2, num1):
    if num8 % i == 0:
        is_valid = False
if is_valid == True:
    print("Your number is prime")
else:
    print("Your number is not prime")

#8)
list5 = [1, 2, 3, 4, 5]
print(list5[0])
print(list5[2])
print(list5[4])

#9)
list6 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(list6[0])
print(list6[1])
print(list6[2])
print(list6[3])
print(list6[4])
print(list6[5])
print(list6[6])
print(list6[7])
print(list6[8])
print(list6[9])
print(list6[10])
print(list6[11])
print(list6[12])
print(list6[13])
print(list6[14])
print(list6[15])
print(list6[16])
print(list6[17])
print(list6[18])
print(list6[19])
