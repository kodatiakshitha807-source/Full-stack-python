#Basic Lambda Function
square=lambda x:x*x
print(square(5))

#Filter Even numbers
Num=[1,2,3,4,5,6]
result=list(filter(lambda x:x%2==0,Num))
print(result)

#Square numbers using map
num=[1,2,3,4,5,6]
result=list(map(lambda x:x*x,num))
print(result)

#Using reduce
from functools import reduce
num=[1,2,3,4,5,6]
result=reduce(lambda a,b:a+b,num)
print(result)

#Call by Object Reference
def change(numbers):
    numbers.append(100)
my_list=[10,20,30]
print("Before function call:",my_list)
change(my_list)
print("After function call;",my_list)