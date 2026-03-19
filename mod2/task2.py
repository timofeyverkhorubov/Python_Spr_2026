a = int(input().strip())
perimeter = 4 * a
area = a * a
diagonal = (2 * a * a) ** 0.5   # или a * (2 ** 0.5)
print(f"{perimeter:.2f}, {area:.2f}, {diagonal:.2f}")