import math

X, Y = map(int, input().split())
# 몫과 나머지
# / 연산자 사용x
# //, % 만으로 계산
# 백분율 -> (Y / X) * 100 -> (Y * 100) // X
Z = (Y * 100) // X

if (99 - Z) == 0:
    print(-1)
else:
    answer = math.ceil(((X * (Z + 1)) - 100 * Y) / (99 - Z))
    print(answer if answer >= 0 else -1)