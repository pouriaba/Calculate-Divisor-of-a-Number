x = int(input("input a number :"))
n = 1
li = []
while n <= x:
    if x % n == 0:
        li.append(n)
    n += 1
print(li)

