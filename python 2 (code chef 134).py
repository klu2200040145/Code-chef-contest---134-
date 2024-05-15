T = int(input())
R = []

S = 45

for _ in range(T):
    N = int(input())

    F = N // 9
    Rm = N % 9

    result = F * S + (Rm * (Rm + 1)) // 2

    R.append(result)

for res in R:
    print(res)
