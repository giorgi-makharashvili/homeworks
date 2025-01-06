#2)
def sum(num1,num2):
    print(num1 + num2)
sum(40,60)

#3)
def even_odd(num):
    if num % 2==0:
        print("number is even")
    else:
        print("number is odd")
even_odd(19)

#4)
def reverse_string(x):
    print(x[::-1])
reverse_string("goaisbest")

#5)
def maximum(list):
    maximum_value = list[0]
    for i in list:
        if i > maximum_value:
            maximum_value = i
    print(maximum_value)
maximum([1,2,3,4,5])

#6)
def factorial(num4):
    factorial1 = 1
    for i in range(1, num4 + 1):
        factorial1 *= i
    print(factorial1)
factorial(11)

