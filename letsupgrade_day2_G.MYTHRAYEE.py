#1. LIST AND ITS DEFAULT FUNCTIONS
list1=[1,"mythrayee",0.5,88,2000]
print("the original list is",list1)


#1.#append function
list1.append(35)
print("list after append is",list1)

#2. Extend function
list1.extend([200,"Tamil"])
print("list after extend is",list1)

#3.pop function
list1.pop(2)
print("list after pop is",list1)

#4.remove function
list1.remove(35)
print("list after remove is",list1)

#5. reverse function
list1.reverse()
print("list after reverse is",list1)

#6. insert
list1.insert(6,"python")
print("list after insert is",list1)

#7. index
list1.index(88)
print("list after index is",list1)



##2) DICTIONARY AND ITS DEFAULT FUNCTIONS
#create a dictionary
dict1={1:"mythrayee",2:"tamil Nadu",3:"Chennai",4:"Tamil",5:"2020"}
print("the dictionary is",dict1)

#Dictionary Length
print(len(dict1))

#Adding Items
dict1["roll"]=88
print(dict1)

#pop 
dict1.pop(1)
print(dict1)

 #popitem() remove last elements
dict1.popitem()
print(dict1)

 #he del keyword removes the item with the specified key name:
del dict1[3]
print(dict1)

#copy
dict2=dict1.copy()
print(dict2)

#The dict() Constructor
thisdict = dict(brand="Ford", model="Mustang", year=1964)
print(thisdict)

#fromkeys() Method
#dict.fromkeys(keys, value)
x = ('key1', 'key2', 'key3')
thisdict = dict.fromkeys(x)
print(thisdict)

# Dictionary get() Method
dict3=dict(name="my3",roll=88,place="chennai")
a=dict3.get("name")
print(a)

#keys()
dict3=dict(name="my3",roll=88,place="chennai")
y=dict3.keys()
print(y)

#update
dict3=dict(name="my3",roll=88,place="chennai")
dict3.update({"degree":"ece"})
print(dict3)

#values() Method
dict3=dict(name="my3",roll=88,place="chennai")
z=dict3.values()
print(z)

##3)SET FUNCTIONS
set1={"hello",11.0,22.0,56.5,-1}
print("the set is",set1)

#1.add
set1.add(390)
print("set after addition",set1)


#2.update
set1.update({5,7})
print("set after updation",set1)


#3.remove
set1.remove(390)
print("set after removal",set1)

#4.discard
set1.discard(3900)
print("set after removal",set1)


#5 set operations UNION
set_1={1,2,3,4,5,6,7}
set_2={6,7,8,9,10,11,12}
print("set union",set_1|set_2)


#6 set operations INTERSECTION
set_1={1,2,3,4,5,6,7}
set_2={6,7,8,9,10,11,12}
print("set union",set_1&set_2)



#7 set operations SET DIFFERENCE
set_1={1,2,3,4,5,6,7}
set_2={6,7,8,9,10,11,12}
print("set union",set_1-set_2)


#8 set operation SYMMETRIC DIFFERENCE
set_1={1,2,3,4,5,6,7}
set_2={6,7,8,9,10,11,12}
print("set union",set_1^set_2)

#4) STRINGS AND ITS FUNCTIONS
str="this is python and it is easy13"
print("the string is ",str)


#1) capitlize()
a=str.capitalize()
print(a)

#2)isalnum()
a=str.isalnum()
print(a)

#3)isalpha()
a=str.isalpha()
print(a)

#4)isdigit()
txt = "50800"
x = txt.isdigit()
print(x)

#5))split()
txt = "welcome to the jungle"
x = txt.split()
print(x)


#5) TUPLES
tup=("mythrayee",2020,"python","letsupgrade","maths",99)
print("the tuple is",tup)

#1)len
tup1=("mythrayee",2020,"python","letsupgrade","maths",99)
tup2=("mythrayee","python","letsupgrade","maths",99)
print(len(tup1))

#2 max)
tup2=("mythrayee","python","letsupgrade","maths")
print(max(tup2))

#3 min
tup2=("mythrayee","python","letsupgrade","maths")
print(min(tup2))


