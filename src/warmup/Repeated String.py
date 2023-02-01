import math


def repeatedString(s, n):
    r = n // len(s)
    q = n % len(s)
    c = 0
    ci = s.count("a")
    if r > 0:
        c = c + (r * ci)
    sq = s[0:q]
    c = c + sq.count("a")
    return c


s = "a2b"
n = 1000000000000
print(repeatedString(s, n))
