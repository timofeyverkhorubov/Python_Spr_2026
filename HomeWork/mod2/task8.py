s = input().strip()

s = s + ' '

result = ""
word = ""

for i in range(len(s)):
    if s[i] != ' ':
        word = word + s[i]
    else:
        if word != "":
            result = result + word[len(word) - 1]
            word = ""

print(result)