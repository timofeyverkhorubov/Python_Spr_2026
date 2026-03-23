numbers = list(map(int, input().split()))
K = int(input())

result = [x for x in numbers if x % K == 0]
print(result)