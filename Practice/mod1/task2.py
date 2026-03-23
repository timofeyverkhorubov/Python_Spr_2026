import math

N = int(input())
numbers = list(range(N, N * N + 1))
roots = [math.sqrt(x) for x in numbers]

print(numbers)
print(roots)