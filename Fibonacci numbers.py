i = 0
a, b = 0, 1
while i <= 50:
    a, b = b, a+b
    i += 1
    print(b, end=" ")
