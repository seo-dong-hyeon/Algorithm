# 최소 편집 거리
# row = len(str1), col = len(str2) 2차원 dp 테이블 생성
# dp 테이블 초기화 -> dp[i][0] = i, dp[0][j] = j
# 점화식
# 문자가 같다면 왼쪽 위에 해당하는 수
# if str1[i - 1] == str2[j - 1] -> dp[i][j] = dp[i - 1][j - 1]
# 문자가 다르다면 왼쪽(삽입), 위쪽(삭제), 왼쪽 위(교체) 중 최소값 + 1
# else -> dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1

import sys

A = sys.stdin.readline().rstrip()
B = sys.stdin.readline().rstrip()
lenA = len(A)
lenB = len(B)

# dp 테이블 초기화
dp = [[0] * (lenB + 1) for _ in range(lenA + 1)]
for i in range(1, lenA + 1):
    dp[i][0] = i
for i in range(1, lenB + 1):
    dp[0][i] = i

# 점화식
for i in range(1, lenA + 1):
    for j in range(1, lenB + 1):
        if A[i - 1] == B[j - 1]:    
            # 문자가 같다면 왼쪽 위에 해당하는 수
            dp[i][j] = dp[i - 1][j - 1]
        else:                       
            # 문자가 다르다면 왼쪽(삽입), 위쪽(삭제), 왼쪽 위(교체) 중 최소값 + 1
            dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1

# print(dp)
print(dp[lenA][lenB])

