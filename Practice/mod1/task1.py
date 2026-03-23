n = int(input())
names = []
for _ in range(n):
    names.append(input().strip())

uni = []
lengths = []

for name in names:
    l = len(name)
    if l not in lengths:
        lengths.append(l)
        uni.append(name)

print(names)
print(uni)