#1) nameerror- საელის ცვლადი არ არის შექმნილი, IndexError-ეს ინდექსი არ არის ლისტში, valueerror-value ში არის შეცდომა და სხვა.

#2)
word1 = "goa"

try:
    print(word2)
except:
    print("name error")

#3)
list1 = [1,2,3,4]

try:
    print(list1[5])
except:
    print("index error")

#3)
str1 = "1234g5"
try:
    print(int(str1))
except:
    print("value error")

#4) try/except  გვადგება იმაში რომ თუ რაიმე error გვაქვს კოდში, ის არ შეჩერდეს და დანარჩენი კოდები გაეშვას.