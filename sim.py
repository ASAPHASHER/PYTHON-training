print("Hello, World!")

name = "Alice"
age = 20
print(name, age)

x = input("Enter something: ")
print("You entered:", x)

x_val = 10
if x_val > 5:
    print("Greater")
else:
    print("Smaller")

for i in range(5):
    print(i)

count = 0
while count < 5:
    print(count)
    count += 1

def add(a, b):
    return a + b

print(add(3, 4))

nums = [1, 2, 3]
nums.append(4)
print(nums)

person = {"name": "Bob", "age": 25}
print(person["name"])

class Person:
    def __init__(self, name):
        self.name = name

p = Person("Charlie")
print(p.name)
