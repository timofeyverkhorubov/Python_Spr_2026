phone = input().strip()

result = ""
for i in range(len(phone)):
    char = phone[i]
    if char >= '0' and char <= '9' or char == '+':
        result = result + char

print(result)