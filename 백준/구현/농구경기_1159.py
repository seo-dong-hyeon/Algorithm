import sys

N = int(sys.stdin.readline().rstrip())

# 이름의 성의 개수를 저장
dict_first_cnt = {}
for _ in range(N):
    name = sys.stdin.readline().rstrip()
    first = name[0]
    if first not in dict_first_cnt:
        dict_first_cnt[first] = 0
    dict_first_cnt[first] += 1

# 성이 5개 이상인 것만 저장
answer = []
for first, cnt in dict_first_cnt.items():
    if cnt >= 5:
        answer.append(first)

if len(answer) == 0:
    print("PREDAJA")
else:
    print(''.join(sorted(answer)))
