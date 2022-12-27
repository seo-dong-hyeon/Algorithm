def dfs(cards, visited, cardNum, groupNum):
    visited[cardNum] = groupNum
    nextNum = cards[cardNum]
    if not visited[nextNum]:
        dfs(cards, visited, nextNum, groupNum)


def solution(cards):
    answer = 0

    # 편의를 위해 카드 번호와 인덱스 번호를 맞춤
    n = len(cards)
    for i in range(n):
        cards[i] -= 1

    visited = [0] * n       # 방문 여부
    groupNum = 1            # 그룹 번호
    while True:
        flag = True
        # 아직 방문 안한 상자를 대상으로 dfs 탐색으로 그룹을 부여
        for card in cards:
            if not visited[card]:
                flag = False
                dfs(cards, visited, card, groupNum)
                break
        # 모든 상자가 방문했다면 종료
        if flag:
            break
        groupNum += 1

    # 그룹 번호별 개수 저장
    dic_group = {}
    for i in range(n):
        if visited[i] not in dic_group:
            dic_group[visited[i]] = 0
        dic_group[visited[i]] += 1

    # 그룹 번호 개수 기준으로 정렬
    if len(dic_group) <= 1:
        answer = 0
    else:
        dic_group = sorted(dic_group.items(), key=lambda x:-x[1])
        answer = dic_group[0][1] * dic_group[1][1]

    return answer