a, b, c = map(int, input().split())
n1 = a + b * c
n2 = (a + b) * c
n3 = a * b * c
n4 = a * b + c
n5 = a * (b + c)
print(max(n1, n2, n3, n4, n5))