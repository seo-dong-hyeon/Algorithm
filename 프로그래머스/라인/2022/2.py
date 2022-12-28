from typing import List

def solution(k: int, dic: List[str], chat: str) -> str:
    answer = ''

    dict_slang = {}
    for i in range(len(dic)):
        dict_slang[dic[i]] = True

    words = chat.split()
    for word in words:
        # 비속어 사전에 있으면 바로 교체
        if word in dict_slang:
            answer += ('#' * len(word))
        # 비속어 사전에 없으면
        else:
            dot_cnt = word.count('.')   # 점 개수
            no_dotted = word.split('.') # 점 제거한 문자 리스트
            flag = False                # 특수문자 대체 여부
            # 모든 비속어에 대해
            for i in range(len(dic)):
                slang = dic[i]
                is_find = True          # 점 제거한 문자 원소가 비속어에 포함되어 있는지
                # 점 제거 문자 리스트에 대해
                for j in range(len(no_dotted)):
                    # 공백이면 넘어감
                    if len(no_dotted[j]) == 0:
                        continue
                    # 점 제거한 문자 원소가 비속어에 포함되어 있지 않으면 해당 비속어는 넘어감
                    if slang.find(no_dotted[j]) == -1:
                        is_find = False
                        break
                    # 점 제거한 문자 원소가 비속어에 포함되어 있다면 비속어에서 해당 문자열 제거
                    else:
                        slang = slang.replace(no_dotted[j], '')
                # 모든 문자 원소가 비속어에 포함되어 있으면서 
                # 남은 비속어 문자가 있으면서 
                # 남은 점으로 남은 비속어 문자들을 만들 수 있다면
                # 특수문자 대체
                if is_find == True and len(slang) >= 1 and dot_cnt * k >= len(slang):
                    answer += ('#' * len(word))
                    flag = True
                    break
            # 최종적으로 특수문자 대체가 없었다면 원문자 추가
            if not flag:
                answer += word
        
        answer += ' '

    # 마지막 띄어쓰기 제거
    answer = answer[:-1]

    return answer