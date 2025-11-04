import math
import threading
import multiprocessing
import time
from abc import ABC, abstractmethod
from functools import reduce

x, y, z = 5, 3.14, "Hello"
flag = True
print(x, y, z, flag)

if x > 3:
    print("x > 3")
elif x == 3:
    print("x == 3")
else:
    print("x < 3")

for i in range(3):
    print(i, end=" ")
print()

i = 0
while i < 3:
    print(i, end=" ")
    i += 1
print()

nums = [1, 2, 3, 4, 5]
squares = [n**2 for n in nums]
evens = [n for n in nums if n % 2 == 0]
print(squares, evens)

add = lambda a, b: a + b
print(add(5, 7))

def greet(name="User"):
    return f"Hello, {name}"

print(greet("Alice"))

def factorial(n):
    return 1 if n <= 1 else n * factorial(n-1)

print(factorial(5))

def generator_demo(n):
    for i in range(n):
        yield i*i

for val in generator_demo(5):
    print(val, end=" ")
print()

def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper

@decorator
def say_hi():
    print("Hi")

say_hi()

try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Error:", e)
finally:
    print("Done")

class Animal(ABC):
    def __init__(self, name):
        self._name = name
    @abstractmethod
    def sound(self):
        pass
    def eat(self):
        print(f"{self._name} is eating")

class Dog(Animal):
    def sound(self):
        print("Woof")

class Cat(Animal):
    def sound(self):
        print("Meow")

animals = [Dog("Buddy"), Cat("Milo")]
for a in animals:
    a.sound()
    a.eat()

class Box:
    def __init__(self, value):
        self.__value = value
    def get(self):
        return self.__value
    def set(self, v):
        self.__value = v

b = Box("Generic Box")
print(b.get())

numbers = [1, 2, 3, 4, 5]
sum_all = reduce(lambda a, b: a + b, numbers)
print(sum_all)

try:
    with open("output.txt", "w") as f:
        f.write("Hello File IO")
except Exception as e:
    print(e)

def worker(name):
    for i in range(3):
        print(f"{name} {i}")
        time.sleep(0.1)

t1 = threading.Thread(target=worker, args=("Thread1",))
t2 = threading.Thread(target=worker, args=("Thread2",))
t1.start(); t2.start()
t1.join(); t2.join()

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=worker, args=("Process1",))
    p2 = multiprocessing.Process(target=worker, args=("Process2",))
    p1.start(); p2.start()
    p1.join(); p2.join()

data = [("Alice", 25), ("Bob", 30)]
d = {k: v for k, v in data}
print(d)

nums = [1, 2, 3, 4, 5]
squares = list(map(lambda n: n*n, nums))
filtered = list(filter(lambda n: n > 10, squares))
print(squares, filtered)

total = sum(nums)
avg = total / len(nums)
print("Sum:", total, "Avg:", avg)
