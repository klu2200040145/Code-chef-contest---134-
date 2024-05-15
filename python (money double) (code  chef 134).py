for _ in range(int(input())):
    a, b = map(int, input().split())
    while b != 0:
        if a <= 1000:
            a += 1000
        else:
            a *= 2
        b -= 1
    print(a)