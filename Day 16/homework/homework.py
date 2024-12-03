#2) ნაჩვენებია ნახაზზე.

#3) for ციკლში წინანასწარ ვიცით იტერაციის რაოდენობა, while  ციკლში კი არ ვიცით.

#4)
for i in range(50):
    print("goa is best")

i = 1
while i <=50:
    print("goa is the best")
    i+=1

#5)
i = 1
while i <=10:
    print(i)
    i+=1

#6)
i = 2
while i <=20:
    print(i)
    i+=2

#7)
i = 10
while i > 0:
    print(i)
    i -= 1
print("blast off!")

#8)
correct_password="123"
password = input("enter password : ")
while password != correct_password:
    password = input("enter password : ")
print("password is correct")

#9)
correct_pass = "123"
correct_user = "gio"

passw = input("enter password")
user = input("enter username")
while passw != correct_pass and user != correct_user :
    passw = input("enter password")
    user = input("enter username")
print("username and password is correct")   

#10).
number = int(input("enter number : "))
factorial = 1
i = number
while i>0:
    factorial*= i 
    i-= 1
print(f"The factorial of {number} is {factorial}.")