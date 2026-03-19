n = input().strip()

if not n.isdigit() or int(n) <= 0:
    print("Неверный ввод")
else:
    num = int(n)

    binary = ""
    temp = num
    if temp == 0:
        binary = "0"
    else:
        while temp > 0:
            binary = str(temp % 2) + binary
            temp //= 2

    octal = ""
    temp = num
    if temp == 0:
        octal = "0"
    else:
        while temp > 0:
            octal = str(temp % 8) + octal
            temp //= 8

    hex_digits = "0123456789abcdef"
    hexadecimal = ""
    temp = num
    if temp == 0:
        hexadecimal = "0"
    else:
        while temp > 0:
            hexadecimal = hex_digits[temp % 16] + hexadecimal
            temp //= 16

    print(f"{binary}, {octal}, {hexadecimal}")