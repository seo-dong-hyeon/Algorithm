import sys

N = int(sys.stdin.readline().rstrip())
# 기본 수
base = '666'
# 새로 추가할 단어 길이
length = 1
# 단어들
nums = set()
nums.add(666)

# 모든 단어의 길이가 찾으려는 수보다 작을때까지
while len(nums) < N:
    for i in range(10 ** length):
        # 새로 추가할 단어
        strNum = str(i).zfill(length)
        # 666 앞뒤로 새로 추가할 단어를 붙임
        nums.add(int(base + strNum))
        nums.add(int(strNum + base))
        # 새로 추가할 단어 사이사이에 666을 끼워 넣음
        for j in range(len(strNum)):
            nums.add(int(strNum[:j] + base + strNum[j:]))
    # 새로 추가할 단어 길이 증가
    length += 1

nums = sorted(nums)

print(nums[N - 1])