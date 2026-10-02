# Simple list operations

fruits = ["apple", "banana", "cherry"]
print("Original:", fruits)

fruits.append("mango")
print("append:", fruits)

fruits.insert(1, "orange")
print("insert:", fruits)

fruits.remove("banana")
print("remove:", fruits)

print("pop:", fruits.pop(), "->", fruits)
print("index of orange:", fruits.index("orange"))
print("slice [0:2]:", fruits[0:2])
print("length:", len(fruits))

fruits.sort()
print("sort:", fruits)

fruits.reverse()
print("reverse:", fruits)

more = ["kiwi", "grape"]
print("concatenate:", fruits + more)

fruits.extend(more)
print("extend:", fruits)
print("'kiwi' in list:", "kiwi" in fruits)

squares = [n * n for n in range(1, 6)]
print("comprehension:", squares)
