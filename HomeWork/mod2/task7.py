s = input().strip()
i = input().strip()

count = 0
for char in s:
    if char == i:
        count += 1
    else:
        break

print(count)