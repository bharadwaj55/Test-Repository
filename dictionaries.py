# Simple dictionary examples

student = {"name": "Alice", "age": 21}
print("Original:", student)

student["course"] = "Python"
print("After adding course:", student)

student["age"] = 22
print("After updating age:", student)

for key, value in student.items():
    print(key, "->", value)
