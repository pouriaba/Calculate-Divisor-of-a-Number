x = int(input("input a number :"))
n = 1
l = []
while n <= x:
    if x % n == 0:
        l.append(n)
    n += 1
print(l)