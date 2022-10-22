import sys

N = int(sys.stdin.readline().rstrip())

score1 = [0] * (60 * 48 + 1)
score2 = [0] * (60 * 48 + 1)
t1 = 0
t2 = 0
for _ in range(N):
    num, time = sys.stdin.readline().rstrip().split()
    num = int(num)
    m, s = map(int, time.split(':'))
    t = m * 60 + s
    # 언제 득점했는지 체크만
    if num == 1:
        score1[t] = 1
    else:
        score2[t] = 1

victory1 = 0
victory2 = 0
# 0분 ~ (60 * 48 - 1)분까지
for i in range(60 * 48):
    # 1분 이후부턴 현재 시간 점수에 이전 시간 점수 더하여 계산
    if i != 0:
        score1[i] += score1[i - 1]
        score2[i] += score2[i - 1]
    if score1[i] > score2[i]:
        victory1 += 1
    elif score1[i] < score2[i]:
        victory2 += 1

m1, s1 = str(victory1 // 60), str(victory1 % 60)
m2, s2 = str(victory2 // 60), str(victory2 % 60)

print(m1.zfill(2) + ':' + s1.zfill(2))
print(m2.zfill(2) + ':' + s2.zfill(2))