import sys

N = int(sys.stdin.readline().rstrip())
pattern1, pattern2 = sys.stdin.readline().rstrip().split('*')

for i in range(N):
    S = sys.stdin.readline().rstrip()
    flag = False
    # 문자열의 앞에서 pattern1 길이만큼이 pattern1과 일치하는지 확인
    if len(S) >= len(pattern1) and S[:len(pattern1)] == pattern1:
        S = S[len(pattern1):]
        # 문자열의 뒤에서 pattern2 길이만큼이 pattern2과 일치하는지 확인
        if len(S) >= len(pattern2) and S[len(S) - len(pattern2):] == pattern2:
            flag = True
    print("DA" if flag else "NE")