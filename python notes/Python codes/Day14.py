# Armstrong number
n = int(input())
temp = n
sum = 0
while n > 0:
    dig = n % 10
    sum += dig ** len(str(temp))
    n = n // 10

if temp == sum:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
    
#prime number count
n = int(input("Enter a number: "))
count = 0
for digit in str(n):
    if digit in '2357':
        count += 1
print("Count of prime digits:", count)

#Palindrome
n = int(input())
temp=n
rev=0
while n>0:
    dig=n%10
    rev=rev*10+dig
    n=n//10
if temp==rev:
    print("Palindrome")
else:
    print("Not a Palindrome")

    '''Using a String
    '''
'''s = str(temp)
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")'''
    
#Factorial
n =int(input("enter a number: "))
fact = 1
for i in range(1,n+1):
    fact *=i
print("Factorial= ",fact)

#Vowel or Consonant
c = input("enter a character: ")
vowels = "aeiou"
if c in vowels:
    print(f"{c} is a vowel")
else:
    print(f"{c} is a consonant")
    
#Understanding the conditional statements
#if statement
n=10
if n>0:
    print(f"{n} is a postive number")

#if-else statement
x=12
if x>0:
    print("Positive")
else:
    print("Not Positive")

#if-elif-else statement
n=int(input("enter a value: "))
if n>0:
    print("Positive")
elif n<0:
    print("Negative")
else:
    print("Neutral or Zero")
    
#For Loop
l=[1,2,4,5,5]
print("example-1")
for i in l:
    print(i)

#printing the even numbers between 1 and 11
print('example-2')
for i in range(1,12):
    if i%2==0:
        print(i)
        
#While loop
#Now printing the numbers from 1 to 20
print("example-1")
start=1
end=20
while start<=end:
    print(start)
    start+=1

#Now printing the numbers from 10 to 1
print("example-2")
start=10
end=1
while start>=end:
    print(start)
    start-=1
    
