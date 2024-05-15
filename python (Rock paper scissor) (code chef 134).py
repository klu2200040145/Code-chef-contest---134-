def function(s, n):
    count_two = 0
    i = 1
    while i < n:
        if s[i] == s[i - 1]:
            count_two += 1
            i += 1
        i += 1
    return count_two

t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    s = input()
    res = function(s, n)
    print(n - res)
