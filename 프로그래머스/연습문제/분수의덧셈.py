from math import gcd

def lcm(x, y):
   return x * y // gcd(x,y)
   

def solution(numer1, denom1, numer2, denom2):
    answer = []

    denom = lcm(denom1, denom2)
    numer1 = (denom // denom1) * numer1
    numer2 = (denom // denom2) * numer2
    numer = numer1 + numer2

    _gcd = gcd(numer, denom)
    if _gcd != 1:
        numer = numer // _gcd
        denom = denom // _gcd

    answer.append(numer)
    answer.append(denom)

    return answer