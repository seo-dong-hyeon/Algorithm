def solution(keymap, targets):
    answer = []

    # 자판이 가장 처음 등장한 순서 저장
    alpha_first_dict = {}
    for i in range(len(keymap)):
        for j in range(len(keymap[i])):
            key = keymap[i][j]
            if key not in alpha_first_dict:
                alpha_first_dict[key] = j + 1
            else:
                alpha_first_dict[key] = min(alpha_first_dict[key], j + 1)

    for target in targets:
        cnt = 0
        for t in target:
            if t not in alpha_first_dict:
                cnt = -1
                break
            cnt += alpha_first_dict[t]
        answer.append(cnt)

    return answer
    