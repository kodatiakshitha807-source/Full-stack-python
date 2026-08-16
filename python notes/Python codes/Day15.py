#Function
def Greet():
    print("Welcome to Functions")
Greet()

#Function with parameters
def Greet(name,age):
    print(f"my name is {name}")
    print(f"my age is {age}")
Greet("Akshitha",21)

#Function with return Type
def Add(a,b):
    c=a+b
    return c
result = Add(10,20)
print(result)

#Variable length Arguments
def ItemBillCal(*items):
    print("All items:" ,items)
    print("Total:",sum(items))
ItemBillCal(100,200,300,400)

#Keyword Variable Length Aruguments
def UserInfo(**details):
    print(details)
UserInfo(name="Akshitha",age=23,height=5.7)


    
    