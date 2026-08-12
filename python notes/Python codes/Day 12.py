# Reverse string

n = int(input("Enter n value: "))
original = n
rev = 0
while n > 0:
    r = n % 10
    rev = rev * 10 + r
    n = n // 10
print(f"The reverse of {original} is:", rev)

#Palindrome

n=int(input("Enter the value: "))
original = n
rev = 0
while n > 0:
    r = n % 10
    rev = rev * 10 + r
    n = n // 10
if original == rev:
    print("Given number is palindrome")
else:
    print("Given number is not palindrome")

#using string

n=132
s = str(n)
if s== s[::-1]:
    print("palindrome")
else:
    print("not palindrome")

#Count Even Digits

n=123456
count=0
s=str(n)
for i in s:
    if int(i) % 2==0:
        print(i)
        count=count+1
print("count of even digits is: " ,count)

#Factorial

n=int(input("Enter a number : "))
for i in range (1,n+1):
    if n%1==0:
        print(i)

#count number of factorial

n = int(input("Enter number: "))
count = 0
for i in range(1, n + 1):
    if n % i == 0:
        count = count + 1
print("Number of factors:", count)

# input n=123456 ,oputput=135 642
n = 123456
odd = ""
even = ""
for i in str(n):
    if int(i) % 2 != 0:
        odd += i
    else:
        even += i
print(odd)
print(even[::-1])


