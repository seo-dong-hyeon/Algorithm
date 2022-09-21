from collections import OrderedDict
from bisect import bisect_left

def solution(info, query):
    answer = []
    
    dict_info = OrderedDict()
    for i in range(len(info)):
        lang, job, career, food, score = info[i].split()
        # 여러 조합으로 이루어진 딕셔너리 키
        combs = [(lang, job, career, food)\
                ,(lang, job, career, '-')\
                ,(lang, job, '-', food)\
                ,(lang, job, '-', '-')\
                ,(lang, '-', career, food)\
                ,(lang, '-', career, '-')\
                ,(lang, '-', '-', food)\
                ,(lang, '-', '-', '-')\
                ,('-', job, career, food)\
                ,('-', job, career, '-')\
                ,('-', job, '-', food)\
                ,('-', job, '-', '-')\
                ,('-', '-', career, food)\
                ,('-', '-', career, '-')\
                ,('-', '-', '-', food)\
                ,('-', '-', '-', '-')]
        for comb in combs:
            if comb not in dict_info:
                dict_info[comb] = []
            dict_info[comb].append(int(score))
            
    for key, value in dict_info.items():
        dict_info[key] = sorted(value)
            
    for i in range(len(query)):
        lang, job, career, food_score = query[i].split(' and ')
        food, X = food_score.split()
        if (lang, job, career, food) not in dict_info:
            answer.append(0)
            continue
        # 정렬된 리스트에서 특정 이상/이하의 수 빨리 찾기
        X = int(X)
        scores = dict_info[(lang, job, career, food)]
        answer.append(len(scores) - bisect_left(scores, X))
        
    return answer