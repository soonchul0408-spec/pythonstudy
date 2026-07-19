a = 18
b = 12

while b:
    a, b = b, a % b

print(a)