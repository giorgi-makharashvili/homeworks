#1)
list1 = [2, 4, 6, 8, 10]
list2 = list(map(lambda x: x*2,list1))
print(list2)

#2)
list3 = ["Alice", "Bob", "Charlie"]
list4 = list(map(lambda x: "Hello,"+x,list3))
print(list4)

#3)
list5 = ["apple", "banana", "kiwi"]
list6 = list(map(lambda x: len(x),list5))
print(list6)

#4)
list7 = [-5, 3, -2, 7, 0, 10]
list8 = list(filter(lambda x: x>0,list7))
print(list8)

#5)
list9 = ["pear", "apple", "peach", "grape"]
list10 = list(filter(lambda x: x[0]=="p",list9))
print(list10)

#6)
list11 = [10, 55, 42, 78, 65, 20]
list12 = list(filter(lambda x: x>50,list11))
print(list12)