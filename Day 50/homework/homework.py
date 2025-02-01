#2)
word1 = "goabest"

try:
    print(wird2)
except:
    print("there is name error")

list1 = [1,2,3,4,5,6,7,8,9]

try:
    print(list1[15])
except:
    print("there is index error")

str1 = "1234ggbyuid78t5"
try:
    print(int(str1))
except:
    print("there is value error")

#3)

def summination(list1):
    count = 0
    for i in list1:
        count += int(i)
    return count
