x = 10
y = 5.5
name = "Alice"
is_active = True
my_list = [1, 2, 3, 4, 5]
my_dict = {"key1": "value1", "key2": "value2"}

if x > y:
    print("x is greater than y")
else:
    print("y is greater than x")

for i in range(5):
    print(i)

while x > 0:
    x -= 1
    print(x)

def greet(name):
    return "Hello " + name

result = greet(name)
print(result)

def add(a, b):
    return a + b

sum_result = add(5, 7)
print(sum_result)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I am {self.name} and I am {self.age} years old.")

person1 = Person("Bob", 30)
person1.introduce()

try:
    z = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

for i in my_list:
    print(i)

for key, value in my_dict.items():
    print(f"{key}: {value}")

def fibonacci(n):
    a, b = 0, 1
    while b < n:
        print(b, end=" ")
        a, b = b, a + b

fibonacci(50)

def square(x):
    return x ** 2

squared_result = square(4)
print(squared_result)

is_even = lambda x: x % 2 == 0
print(is_even(4))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

factorial_result = factorial(5)
print(factorial_result)

try:
    file = open("sample.txt", "r")
    content = file.read()
    file.close()
except FileNotFoundError:
    print("File not found")
