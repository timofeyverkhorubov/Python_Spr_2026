domain = input().strip()

part1 = ""
part2 = ""
part3 = ""
current = ""
dots = []

for i in range(len(domain)):
    if domain[i] == '.':
        if dots == []:
            part1 = current
        elif len(dots) == 1:
            part2 = current
        dots.append(i)
        current = ""
    else:
        current = current + domain[i]

if len(dots) == 1:
    part2 = current
elif len(dots) == 2:
    part3 = current

if len(dots) == 2:
    print(part3)
    print(part2)
    print(part1)
elif len(dots) == 1:
    print(part2)
    print(part1)