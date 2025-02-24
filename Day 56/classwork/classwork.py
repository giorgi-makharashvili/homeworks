#1)
list1 = [1,41,43,12,32,555]
list2 = list(filter(lambda x: x>=40,list1))
print(list2)

#2)
list3 = [2,3,4,5,6]
list4 = list(map(lambda x: x**2,list3))
print(list4)

#3)
list5 = ["pear", "apple", "peach", "grape", "gela", "nugzara"]
list6 = list(filter(lambda x: x[-1]=="a",list5))
print(list6)