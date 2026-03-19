s = input().strip()

count_zeros = 0
count_ones = 0

for char in s:
    if char == '0':
        count_zeros += 1
    elif char == '1':
        count_ones += 1

if count_zeros == count_ones:
    print("yes")
else:
    print("no")