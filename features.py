# Metaclass
class M(type):
    def __new__(cls, name, bases, attrs):
        attrs["created_by_metaclass"] = True
        return super().__new__(cls, name, bases, attrs)

class A(metaclass=M):
    pass


# Descriptor
class D:
    def __get__(self, obj, objtype=None):
        return obj._x
    def __set__(self, obj, value):
        obj._x = value

class B:
    x = D()


# Parameterized Decorator
def deco(msg):
    def wrapper(fn):
        def inner(*a, **k):
            return msg + " " + fn(*a, **k)
        return inner
    return wrapper


# Class Decorator
def add_attr(cls):
    cls.extra = "added"
    return cls

@add_attr
class C:
    @deco("hello")
    def f(self):
        return "world"


# Context Manager
class CM:
    def __enter__(self):
        return "inside"
    def __exit__(self, a, b, c):
        pass


# Custom Iterator
class MyIter:
    def __init__(self, n):
        self.n = n
    def __iter__(self):
        return self
    def __next__(self):
        if self.n == 0:
            raise StopIteration
        self.n -= 1
        return self.n


# Generator Pipeline
def g1():
    for i in range(3):
        yield i

def g2(it):
    for x in it:
        yield x * 2


# Simple Coroutine
def coro():
    x = yield
    yield x * 10


# GIL demonstration (threads competing)
import threading

counter = 0
def task():
    global counter
    for _ in range(100000):
        counter += 1

t1 = threading.Thread(target=task)
t2 = threading.Thread(target=task)
t1.start(); t2.start()
t1.join(); t2.join()


# Run everything
print(A.created_by_metaclass)
b = B(); b.x = 42; print(b.x)
print(C().f(), C.extra)

with CM() as v:
    print(v)

print(list(MyIter(3)))
print(list(g2(g1())))

c = coro()
next(c)
print(c.send(5))

print(counter)
