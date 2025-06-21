t = int(input())
for i in range(t):
    n, x = map(int, input().split())
    a = [int(i) for i in input().split()]
    if a.count(1) == 0:
        print('YES')
    else:
        ind1 = a.index(1)
        ind2 = n - 1 - a[::-1].index(1)
        mx = ind2 - ind1 + 1

        if x >= mx:
            print('YES')
        else:
            print('NO')
