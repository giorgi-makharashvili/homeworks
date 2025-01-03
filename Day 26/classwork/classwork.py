

def greet(name):
    print("gamarjoba",name)

greet("gio")

def manual_range(start,end,step):
    for i in range(start,end,step):
        if i % 2 == 0:
            print(i)
        else:
            print("other nums are odd")

manual_range(2,8,2)
manual_range(2,10,2)
manual_range(2,9,3)
manual_range(6,12,2)
manual_range(7,20,4)

def manual_len(list):
    lenght=0
    for a in list:
        lenght+=1
    print("The lenght is", lenght)

list=[1,2,3,4,5,6,7,8,9,10]
manual_len(list)
