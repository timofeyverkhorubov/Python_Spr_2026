prices = list(map(int, input().split()))
K, M = map(int, input().split())

discount = [p - (p // K) * M for p in prices]

print(prices)
print(discount)