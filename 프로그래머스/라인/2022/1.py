from typing import List
import math

def solution(queries: List[List[int]]) -> int:
    answer = 0

    dict_squared = {}
    dict_list_size = {}
    dict_ele_size = {}
    squared = []
    for i in range(35):
        squared.append(int(math.pow(2, i)))

    for num, size in queries:
        # 해당 번호의 배열이 없는 경우
        if num not in dict_squared:
            # 배열 크기 결정
            for i in range(35):
                if squared[i] >= size:
                    dict_squared[num] = i
                    break
            dict_list_size[num] = squared[dict_squared[num]]
            # 배열에 원소 넣기
            dict_ele_size[num] = size
        # 해당 번호의 배열이 있는 경우
        else:                 
            now_size = dict_ele_size[num]
            new_size = now_size + size
            # 배열의 크기가 추가된 원소들의 크기보다 큰 경우 그냥 추가
            if dict_list_size[num] >= new_size:
                dict_ele_size[num] = new_size
            # 배열의 크기가 추가된 원소들의 크기보다 작은 경우
            else:
                # 배열 크기 결정
                for i in range(dict_squared[num], 35):
                    if squared[i] >= new_size:
                        dict_squared[num] = i
                        break
                dict_list_size[num] = squared[dict_squared[num]]
                # 배열에 원소 넣기
                dict_ele_size[num] = new_size
                # 기존 배열 원소 복사
                answer += now_size

        

    return answer