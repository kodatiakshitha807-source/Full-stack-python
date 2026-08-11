#Topics: Set, dictionary,boolean, None,Type conversion(implicit,explicit).
'''
1. Set (set) :
What is a Set?
A set is a built-in Python data type used to store unique elements.
Does not allow duplicate values
Mutable (elements can be added or removed)
Unordered (items do not have a fixed position)
Represented using curly braces {}
Set elements must be immutable (e.g., int, float, string, tuple)

Syntax
       set_name = {item1, item2, item3}
Example
student_ids = {101, 102, 103, 104}

print(student_ids)
Possible Output
{104, 101, 102, 103}
Note: The order may change because sets are unordered.

Checking the Data Type
student_ids = {101,102,103,104}

print(type(student_ids))
Output:
<class 'set'>

Duplicate Values are Automatically Removed
student_ids = {101,102,103,101}

print(student_ids)
Output
{101, 102, 103}
The duplicate value 101 is removed automatically.

Empty Set
Many beginners make this mistake.
Incorrect
s = {}

print(type(s))
Output
<class 'dict'>
{} creates an empty dictionary, not a set.

Correct
s = set()

print(s)
print(type(s))
Output
set()
<class 'set'>

Set Properties
Property
Description
Ordered
❌ No
Indexed
❌ No
Mutable
✅ Yes
Duplicate Values
❌ Not Allowed
Representation
{}


Example:
fruits = {"Apple","Mango","Orange"}

print(fruits)

Adding an Element
fruits = {"Apple","Mango"}

fruits.add("Orange")

print(fruits)
Output
{'Apple', 'Mango', 'Orange'}

2. Dictionary (dict):
What is a Dictionary?
A dictionary stores data in the form of key-value pairs.
Each key is associated with a value.
Example
Name  → Raju
Age   → 21
City  → Hyderabad

Syntax
          dictionary_name = {
              key1:value1,
              key2:value2
           }
Example
student = {
    "name":"Raju",
    "age":21,
    "city":"Hyderabad"
}

Dictionary Properties:
Ordered (Python 3.7+)
Mutable
Keys must be unique
Values may be duplicated
Represented using {}

Accessing Values
student = {
    "name":"Raju",
    "age":21,
    "city":"Hyd"
}

print(student["name"])
Output
Raju

print(student["age"])
Output
21

Accessing a Non-Existing Key
print(student["marks"])
Output
KeyError: 'marks'
The key "marks" does not exist.

Using get() Method
The get() method safely returns the value if the key exists.
print(student.get("name"))
Output
Raju

If the key does not exist,
print(student.get("marks"))
Output
None
No error is generated.

Dictionary Example
student = {
    "name":"Raju",
    "age":21,
    "city":"Hyd"
}

print(student["name"])
print(student["city"])
Output
Raju
Hyd

Dictionary Representation
Key        Value

name   →   Raju

age    →   21

city   →   Hyd

Set vs Dictionary
Set                                          Dictionary
Stores only values                           Stores key-value pairs
Duplicate values not allowed                 Duplicate keys not allowed
Uses {}                                      Uses {}
Empty set → set()                            Empty dictionary → {}

3. Boolean (bool):
What is Boolean?
Boolean data type represents only two values.
True
False

Example:
print(True)
print(False)
Output
True
False

Comparison Operators Return Boolean Values
print(10 == 10)
Output
True

print(10 > 5)
Output
True

print(10 < 20)
Output
True

print(10 < 5)
Output
False

Boolean Variables
is_logged_in = True

is_admin = False

print(is_logged_in)

4. None (NoneType):
What is None?
None represents the absence of a value or no value.
It is the only value of the NoneType data type.

Example
payment_status = None

order_confirmation = None

print(payment_status)
Output
None

Checking None
x = None

print(type(x))
Output
<class 'NoneType'>

Real-Time Example
employee_name = None

print(employee_name)
Later,
employee_name = "Raju"
Now the variable contains an actual value.

5. Type Casting:
What is Type Casting?
Type casting is the process of converting one data type into another.
Example
Integer → Float

String → Integer

Float → String

Types of Type Casting
Implicit Type Casting
Explicit Type Casting

1. Implicit Type Casting (Automatic)
Python automatically converts a smaller compatible type into a larger compatible type during an operation.
Example
a = 10        # int

b = 12.5      # float

print(a + b)
Output
22.5
Python converts
10 → 10.0
before performing the addition.

Another Example
a = True

b = 5

print(a + b)
Output
6
Because
True = 1

False = 0

2. Explicit Type Casting (Manual)
The programmer converts the data type using built-in functions.
Common conversion functions
Function
Description
int()
Convert to integer
float()
Convert to float
str()
Convert to string
bool()
Convert to boolean
list()
Convert to list
tuple()
Convert to tuple
set()
Convert to set
dict()
Convert to dictionary


Integer Conversion
a = 10

print(a, type(a))
Output
10 <class 'int'>
Convert to float
b = float(a)

print(b, type(b))
Output
10.0 <class 'float'>

Convert to string
c = str(a)

print(c, type(c))
Output
10 <class 'str'>

Convert to boolean
d = bool(a)

print(d, type(d))
Output
True <class 'bool'>

Float Conversion
a = 10.5
Convert to integer
print(int(a))
Output
10
Note: int() truncates the decimal part; it does not round the value.

Convert to string
print(str(a))
Output
'10.5'

Convert to boolean
print(bool(a))
Output
True

String Conversion
x = "10"

print(int(x))
Output
10

print(float(x))
Output
10.0

print(bool(x))
Output
True
Because the string is not empty.

Boolean Conversion
print(int(True))
print(int(False))
Output
1
0

print(float(True))
Output
1.0

print(str(False))
Output
False

Converting Sequence Types
List to Tuple
numbers = [10,20,30]

print(tuple(numbers))
Output
(10, 20, 30)

Tuple to List
numbers = (10,20,30)

print(list(numbers))
Output
[10, 20, 30]

List to Set
numbers = [10,20,20,30]

print(set(numbers))
Output
{10, 20, 30}
Duplicate values are removed.

String to List
name = "Python"

print(list(name))
Output
['P', 'y', 't', 'h', 'o', 'n']

String to Tuple
name = "Python"

print(tuple(name))
Output
('P', 'y', 't', 'h', 'o', 'n')

String to Set
name = "Python"

print(set(name))
Output (order may vary)
{'P', 'y', 't', 'h', 'o', 'n'}

Dictionary Conversion
A dictionary requires an iterable containing key-value pairs.
Correct Example
data = [
    ("name", "Raju"),
    ("age", 23)
]

student = dict(data)

print(student)
Output
{'name': 'Raju', 'age': 23}

Incorrect Example
dict([1,2])
Output
TypeError
Because each element must contain exactly two values (a key and a value).

Important Notes
This is invalid because an integer is not iterable.
list(10)
Output
TypeError: 'int' object is not iterable
Similarly,
tuple(10)
set(10)
also produce a TypeError.
'''
# converting interger to float,string,boolean
num = 2

# int to float
print(float(num))

# int to string
print(str(num))

# int to boolean
print(bool(num))

#converting float to int,string,boolean
price = 3.1

# float to int
print(int(price))

# float to string
print(str(price))

# float to boolean
print(bool(price))

#conerting string to boolean,list,tuple,set
name = "power"

# string to boolean
print(bool(name))

# string to list
print(list(name))

# string to tuple
print(tuple(name))

# string to set
print(set(name))

#converting list to string,tuple,set,boolean
numbers = [1,2,3,4]

# list to string
print(str(numbers))

# list to tuple
print(tuple(numbers))

# list to set
print(set(numbers))

# list to boolean
print(bool(numbers))

#conerting tuple to string,list,set,bollean
t = (1,2,3,4)

print(str(t))
print(list(t))
print(set(t))
print(bool(t))

#converting set into string,list,tuple,boolean
s = {3,4,5,6}

print(str(s))
print(list(s))
print(tuple(s))
print(bool(s))

#converting dictionary into string,list,tuple,set,boolean
student = {
    1:"Python",
    2:"Java",
    3:"SQL"
}

print(str(student))
print(list(student))
print(tuple(student))
print(set(student))
print(bool(student))

#converting boolean into string,int,float
value = False

print(int(value))
print(float(value))
print(str(value))
