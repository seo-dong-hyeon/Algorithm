import sys

S = sys.stdin.readline().rstrip()
dict_alpha_cnt = {}

alphas = []
# 알파벳 개수 저장
# 알파벳이 짝을 이루면 알파벳 리스트로 옮김
for alpha in S:
    if alpha not in dict_alpha_cnt:
        dict_alpha_cnt[alpha] = 0
    dict_alpha_cnt[alpha] += 1
    if dict_alpha_cnt[alpha] == 2:
        alphas.append(alpha)
        dict_alpha_cnt[alpha] = 0

alpha_middle = []
flag = True
# 알파벳 개수 검사
for alpha, cnt in dict_alpha_cnt.items():
    if cnt == 0:
        continue
    if cnt == 1:
        # 알파벳이 1개인 경우가 2개 이상이면 팰린드롬 불가
        # 아니면 따로 가운데에 넣을 알파벳 리스트에 저장
        if len(alpha_middle) != 0:
            print("I'm Sorry Hansoo")
            flag = False
            break
        alpha_middle.append(alpha)

if flag:
    # 짝을 이루는 알파벳 리스트가 없다면
    # 가운데에 넣을 알파벳 리스트도 없다면 팰린드롬 불가
    # 가운데에 넣을 알파벳은 있다면 해당 알파벳이 정답 문자열
    if len(alphas) == 0:
        if len(alpha_middle) == 0:
            print("I'm Sorry Hansoo")
        else:
            print(alpha_middle[0])
    else:
        # 알파벳 정렬 후 첫번째 알파벳을 기준으로 둠
        alphas = sorted(alphas)
        answer = alphas[0] * 2
        # 알파벳 리스트를 순회하면서
        for i, alpha in enumerate(alphas):
            if i == 0:
                continue
            # i번 위치에 새로운 알파벳 쌍을 집어 넣어 팰린드롬을 만듦
            answer = answer[:i] + (alpha * 2) + answer[i:]
        # 순회 종료 후 가운데에 넣을 알파벳 검사
        # 알파벳이 있다면 가운데에 넣음
        if len(alpha_middle) != 0:
            middle_idx = len(answer) // 2
            answer = answer[:middle_idx] + alpha_middle[0] + answer[middle_idx:]
        print(answer)
