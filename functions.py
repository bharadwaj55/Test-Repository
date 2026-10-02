# Simple function examples

def greet(name):
    return "Hello, " + name + "!"


def add(a, b):
    return a + b


def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result = result * i
    return result

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b


print(greet("Alice"))
print("2 + 3 =", add(2, 3))
print("5! =", factorial(5))
print("10 - 5 =", subtract(10, 5))
print("4 * 6 =", multiply(4, 6))