import sys

N = int(sys.stdin.readline().rstrip())

nums = []
for _ in range(N):
    S = sys.stdin.readline().rstrip()
    num = ""
    for i in range(len(S)):
        if S[i].isdigit():
            num += S[i]
        else:
            if len(num) != 0:
                nums.append(int(num))
                num = ""
    # 마지막에 완료가 안 된 문자열 처리
    if len(num) != 0:
        nums.append(int(num))
        num = ""

nums.sort()
for num in nums:
    print(num)