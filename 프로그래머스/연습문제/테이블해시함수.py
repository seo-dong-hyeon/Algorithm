def solution(data, col, row_begin, row_end):
    answer = 0

    # 필요한 데이터로 분류
    # tuples[i][j] = [[j행 i열 데이터, j행 0열 데이터, j]
    tuples = [[] for _ in range(len(data[0]))]
    for i in range(len(data[0])):
        _col = []
        for j in range(len(data)):
            _col.append([data[j][i], data[j][0], j])
        tuples[i].extend(_col)

    # 필요한 데이터만 가져옴
    # 각 행의 i열 데이터를 기준으로 오름차순, 동일하면 기본키를 기준으로 내림차순 정렬
    tuples = tuples[col - 1]
    tuples = sorted(tuples, key=lambda x :[x[0], -x[1]])

    # 정렬된 데이터의 행번호로 data에서 행들을 가져옴
    sortedData = []
    for _, _, idx in tuples:
        sortedData.append(data[idx])

    # 해시값 만들기
    S = []
    for i in range(row_begin, row_end + 1):
        S_i = 0
        for j in range(len(data[0])):
            S_i += sortedData[i - 1][j] % i
        S.append(S_i)

    # XOR 연산
    for i in range(len(S)):
        answer = answer ^ S[i]

    return answer