#1)
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num = int(input("enter your number: "))
if num >=  0 and num < 10:
    print(list[num])
elif num >= -10 and num <= -1:
    print(list[num])
else:
    print("wrong number")

#2)
list1 = [2, 4 ,6, 8, 10, 12, 14, 16, 18, 20]
for i in list1:
    print(i * 2)
    print(i / 2)


