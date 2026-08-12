# 3*3 matrics
# * * *
# * * *
# * * *

r=3
for i in range (0,3):
    for j in range(0,3):
        print('*',end=" ")
    print()

# * * * *
# * * * *

r=2
c=4
for i in range(0,r):
    for j in range (0,c):
        print('*' ,end=" ")
    print()

# *
# * *
# * * *

for i in range (4):
    for j in range (i):
        print('*' , end=" ")
    print()

#    *
#   * *
#  * * *
# * * * *

r=4
for i in range(1,r+1):
    for k in range (r-i):
        print(' ' , end=" ")
    for i in range(i):
        print('*' ,end=" ")
    print()

# 1
# 2 2
# 3 3 3

for i in range(1,5):
    for j in range (i):
        print(i, end=" ")
    print()
# 1
# 1 2
# 1 2 3
# 1 2 3 4

for i in range(1,5):
    for j in range (1, i+1):
        print(i, end=" ")
    print()

# * * * *
# * *
# * *
# * * * *
r=4
for i in range(r):
    for j in range(r):
        if i==0 or i==r-1 or j==0 or j==r-1:
            print('*' , end=" ")
        else:
            print('', end='')
    print()