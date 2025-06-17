from collections import Counter
from fractions import Fraction
from string import ascii_lowercase


n = int(input())
line = input()
counts = Counter(line)
res = [counts.get(symbol, 0) for symbol in ascii_lowercase]
s = sum(res)
probability = [Fraction(count) / Fraction(s) for count in res]
l = Fraction(0)
r = Fraction(1)
eMap = {}
v = Fraction(0)
for i in range(len(probability)):
    eMap[ascii_lowercase[i]] = (v, v + probability[i])
    v += probability[i]

for i in range(len(line)):
    symbol = line[i]
    newR = l + (r - l) * eMap[symbol][1]
    newL = l + (r - l) * eMap[symbol][0]
    l = newL
    r = newR
l_n, l_d = l.numerator, l.denominator
r_n, r_d = r.numerator, r.denominator
q = 1
while True:
    d = 2 ** q
    l_m = l_n * d
    r_m = r_n * d - 1
    mini = (l_m + l_d - 1) // l_d
    maxi = r_m // r_d

    if mini <= maxi:
        p = mini
        if l <= Fraction(p, d) < r:
            print(bin(p)[2:].zfill(q))
            break
    q += 1
