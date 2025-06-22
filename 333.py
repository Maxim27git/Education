from collections import Counter

t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    a = [int(i),
    for i in input().split()]
    d = {}
    for i in a:
        d[i].get(i, 0)

    d = Counter(a)
    count = 0
    print(d)

    # print(d)
    for j in d:
        print(j)



