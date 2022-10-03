import sys
from string import ascii_uppercase

S = sys.stdin.readline().rstrip()
dict_upper_idx = {}     # 대문자 알파벳 -> 순서
dict_lower_idx = {}     # 소문자 알파벳 -> 순서
dict_idx_upper = {}     # 순서 -> 대문자 알파벳
dict_idx_lower = {}     # 순서 -> 소문자 알파벳
answer = ""

# 알파벳의 순서, 순서에 따른 알파벳 저장
for i, alpha in enumerate(ascii_uppercase):
    dict_upper_idx[alpha] = i
    dict_lower_idx[alpha.lower()] = i
    dict_idx_upper[i] = alpha
    dict_idx_lower[i] = alpha.lower()

for i in range(len(S)):
    # 대문자
    if S[i] in dict_upper_idx:
        idx = dict_upper_idx[S[i]]
        # 13글자를 밀어서 새 위치의 알파벳을 가져옴
        idx = (idx + 13) % 26
        answer += dict_idx_upper[idx]
    # 소문자
    elif S[i] in dict_lower_idx:
        idx = dict_lower_idx[S[i]]
        # 13글자를 밀어서 새 위치의 알파벳을 가져옴
        idx = (idx + 13) % 26
        answer += dict_idx_lower[idx]
    # 숫자면 그냥 저장
    else:
        answer += S[i]

print(answer)
