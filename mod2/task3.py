a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

if a <= b <= c or c <= b <= a:
    print(b)
elif b <= a <= c or c <= a <= b:
    print(a)
else:
    print(c)