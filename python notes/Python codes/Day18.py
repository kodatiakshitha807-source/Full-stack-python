#Generator
def count_up_to(n):
    count = 1
    while count <=n:
        yield count
        count += 1
counts = count_up_to(5)
print(next(counts))
print(next(counts))
print(next(counts))

#Square numbers using Generator
def square_num(n):
    for i in range(n):
        yield i*i
squares=square_num(5)
print(next(squares))
print(next(squares))

#List Comprehension
num=[1,2,3,4,5,6]
squares=[x*x for x in num]
print(squares)

# Flatten a list of product color options
products_colors = [
{"name": "Laptop", "colors": ["Silver", "Black"]},
{"name": "Phone", "colors": ["Gold", "Blue"]}
]
all_colors = [color for product in products_colors for color
in product["colors"]]
print(all_colors)

#Show available product names with discounted prices
products_data = [
{"name": "Laptop", "price": 1000, "stock": 3},
{"name": "Phone", "price": 800, "stock": 0},
{"name": "Tablet", "price": 450, "stock": 5}
]
result = [f"{p['name']} - ${p['price'] * 0.9:.2f}" for p in
products_data if p["stock"] > 0]
print(result)