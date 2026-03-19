def check_palindrome(s):
    chars = []
    for c in s:
        chars.append(c)

    for i in range(len(chars) // 2):
        if chars[i] != chars[len(chars) - 1 - i]:
            print("Нельзя составить палиндром")
            return

    print(s)

check_palindrome(input().strip())