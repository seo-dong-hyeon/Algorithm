from collections import deque
from string import ascii_lowercase

# 섹션 묶기
def bfs(maps, section, x, y, num):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    dq = deque()
    dq.append([x, y])
    section[x][y] = num
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < len(section) and ny >= 0 and ny < len(section[0]) and maps[nx][ny] != '.' and section[nx][ny] == -1:
                dq.append([nx, ny])
                section[nx][ny] = num

    return section


def solution(maps):
    answer = 0

    section = [[-1] * len(maps[0]) for _ in range(len(maps))]
    section_num = 0

    # 각 위치마다 섹션 번호 부여
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != '.' and section[i][j] == -1:
                section = bfs(maps, section, i, j, section_num)
                section_num += 1

    # 각 섹션마다 도시 리스트 만들기
    dict_section_member = {}
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if section[i][j] != -1:
                if section[i][j] not in dict_section_member:
                    dict_section_member[section[i][j]] = []
                dict_section_member[section[i][j]].append(maps[i][j])

    # 알파벳의 순서 저장
    dict_alpha_num = {}
    alphabets = list(ascii_lowercase)
    for i in range(len(alphabets)):
        alphabets[i] = alphabets[i].upper()
        dict_alpha_num[alphabets[i]] = i

    # section_mem_cnt[i]['A'] = i번 섹션에서 'A' 도시의 개수
    section_mem_cnt = [{} for _ in range(section_num + 1)]
    # section_max_mem[i] = i번 섹션에서 가장 넓은 영역을 가진 도시
    section_max_mem = [''] * (section_num + 1)
    # section_max_cnt[i] = i번 섹션에서 가장 넓은 영역을 가진 도시의 영역 크기
    section_max_cnt = [0] * (section_num + 1)
    
    # 모든 섹션마다
    for i in range(section_num):
        max_cnt = 0
        max_mem = ''
        # 모든 알파벳에 대해 검사
        for alphabet in alphabets:
            if alphabet in dict_section_member[i]:
                # 해당 섹션에서 해당 알파벳(도시)의 개수(영역 크기)를 구함
                section_mem_cnt[i][alphabet] = dict_section_member[i].count(alphabet)
                # 도시의 영역이 가장 큰 개수보다 많다면 갱신
                if section_mem_cnt[i][alphabet] > max_cnt:
                    max_cnt = section_mem_cnt[i][alphabet]
                    max_mem = alphabet
                # 도시의 영역이 가장 큰 개수와 같다면
                if section_mem_cnt[i][alphabet] == max_cnt:
                    # 더 뒤에 있는 알파벳일때만 갱신
                    if dict_alpha_num[alphabet] > dict_alpha_num[max_mem]:
                        max_cnt = section_mem_cnt[i][alphabet]
                        max_mem = alphabet
        # 최종적으로 갱신된 도시와 개수를 각각 저장
        section_max_mem[i] = max_mem
        section_max_cnt[i] = max_cnt

    # 새로운 지도 리스트 만들기
    new_maps = [[''] * len(maps[0]) for _ in range(len(maps))]
    # 기존 지도를 탐색하면서
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            # 도시면
            if maps[i][j] != '.':
                # 해당 위치의 섹션 번호와 
                # 해당 섹션 번호에서 현재 탐색하는 도시의 영역 크기를 가져옴
                section_num = section[i][j]
                cnt = section_mem_cnt[section_num][maps[i][j]]
                # 현재 탐색하는 도시의 크기보다 
                # 미리 지정된 해당 섹션에서의 가장 큰 영역의 크기보다 작다면
                # 해당 위치는 미리 지정된 가장 큰 영역의 도시로 교체(가장 큰 영역의 도시가 점령)
                if section_max_cnt[section_num] > cnt:
                    new_maps[i][j] = section_max_mem[section_num]
                # 현재 탐색하는 도시의 크기와 
                # 미리 지정된 해당 섹션에서의 가장 큰 영역의 크기가 같다면
                # 해당 위치는 미리 지정된 가장 큰 영역의 도시로(원래 위치)
                elif section_max_cnt[section_num] == cnt:
                    new_maps[i][j] = maps[i][j]
            # 도시가 아니면 그냥 저장
            else:
                new_maps[i][j] = maps[i][j]

    # 새로운 지도 리스트에서
    # 각 도시들의 개수를 저장
    dict_mem_cnt = {}
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if new_maps[i][j] == '.':
                continue
            if new_maps[i][j] not in dict_mem_cnt:
                dict_mem_cnt[new_maps[i][j]] = 0
            dict_mem_cnt[new_maps[i][j]] += 1

    # 도시들의 개수 중 가장 큰 것을 정답으로
    for value in dict_mem_cnt.values():
        answer = max(answer, value)

    return answer

# print(solution(["AABCA.QA", "AABC..QX", "BBBC.Y..", ".A...T.A", "....EE..", ".M.XXEXQ", "KL.TBBBQ"]))
# print(solution(["XY..", "YX..", "..YX", ".AXY"]))