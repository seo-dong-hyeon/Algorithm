# 문자열 그룹화
import sys

S = sys.stdin.readline().rstrip()
before = int(S[0])      # 이전 문자(첫 문자로 시작)
groupCnt = [0, 0]       # 그룹 개수
groupCnt[before] += 1   # 첫 문자의 그룹 개수 일단 증가

for i in range(1, len(S)):
    now = int(S[i])         # 현재 탐색 문자
    if now!= before:        # 현재 문자와 이전 문자가 다르다면
        groupCnt[now] += 1  # 현재 문자의 새로운 그룹 생성
        before = now        # 이전 문자를 현재 문자로

print(min(groupCnt))