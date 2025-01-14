#1)
list = [ i for i in range(1, 101)]
print(list)

#2)
list1 = [i for i in range(1,101) if i%2 != 0]
print(list1)

#3)
list2 = ["max","george", "nika","data","saba"]
list3 = ["#" + i.replace("a","") for i in list2]
print(list3)