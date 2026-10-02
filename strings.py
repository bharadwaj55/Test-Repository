# Simple string operations

text = "  Git is fun  "
print("Original:", repr(text))
print("strip:", text.strip())

s = text.strip()
print("upper:", s.upper())
print("lower:", s.lower())
print("title:", s.title())
print("replace:", s.replace("fun", "awesome"))
print("split:", s.split())
print("join:", "-".join(s.split()))
print("length:", len(s))
print("first char:", s[0], "| last char:", s[-1])
print("slice [0:3]:", s[0:3])
print("reversed:", s[::-1])
print("find 'is':", s.find("is"))
print("startswith 'Git':", s.startswith("Git"))
print("count 'i':", s.count("i"))
print("concatenate:", s + " and powerful")

name = "Alice"
print(f"f-string: Hello, {name}!")
