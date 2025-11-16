class UpperCaseDescriptor:
    def __get__(self, instance, owner):
        return instance.__dict__.get("name")

    def __set__(self, instance, value):
        instance.__dict__["name"] = value.upper()


class Meta(type):
    def __new__(cls, name, bases, attrs):
        attrs["created_by"] = "MetaClass"
        return super().__new__(cls, name, bases, attrs)


Base = type("Base", (), {"base_value": 10})


class Person(Base, metaclass=Meta):
    name = UpperCaseDescriptor()

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return f"{self.name} is {self.age} years old"

    def __add__(self, other):
        return self.age + other.age


class Employee(Person):
    def info(self):
        return super().info() + f" and works at {self.company}"


p1 = Person("alice", 25)
p2 = Person("bob", 30)

e = Employee("john", 28)
e.company = "OpenAI"

print(p1.info())
print(p2.info())
print(e.info())
print(p1 + p2)
print(Person.created_by)
print(Person.base_value)
