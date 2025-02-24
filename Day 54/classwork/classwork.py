# 1) რომლებია mutable მონაცემთა ტიპები?
#list,dictionary,set
# 2) რომლებია immutable მონაცემთა ტიპები?
#int, str, complex, float, tuple, .
# 3) რა ეწოდება lambda ფუნქციას მეორენაირად?
#მეორენაირად "ანონიმური ფუნქცია" ეწოდება.
# 4) რა განსხვავებაა map'სა და filter'ს შორის?
# Mapყველა ელემენტზე ამუშავებს ფუქნციას, filter იმათზე რაც ფუნქციის პირობიდან გამომდინარეობს.
# 5) რა ჰქვია ორი სტრინგის შეერთებას?
# კონკადინაცია

#map
#1)
list1 = [1, 2, 3, 4, 5]
list2 = list(map(lambda x: x ** 2,list1))
print(list2)

#2)
list3 = [0, 20, 30, 40]
list4 = list(map(lambda i: (i * 1.8)+32,list3 ))
print(list4)

#3)
list5 = ["hello", "world", "python"]
list6 = list(map(lambda v: v.capitalize(),list5))
print(list6)

#filter
#1)
list7 = [1, 2, 3, 4, 5, 6, 7, 8]
list8 = list(filter(lambda x: x%2 == 0,list7))
print(list8)

#2)
list9 = ["cat", "house", "tree", "car"]
list10 = list(filter(lambda x: len(x)>=4,list9))
print(list10)

#3)
list11 = [3, 9, 15, 22, 27, 30]
list12 = list(filter(lambda x: x%3==0,list11))
print(list12)