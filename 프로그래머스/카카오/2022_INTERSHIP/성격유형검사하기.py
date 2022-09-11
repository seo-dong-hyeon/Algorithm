def solution(survey, choices):
    answer = ''
    dict_score = {}
    dict_score['R'] = 0
    dict_score['T'] = 0
    dict_score['C'] = 0
    dict_score['F'] = 0
    dict_score['J'] = 0
    dict_score['M'] = 0
    dict_score['A'] = 0
    dict_score['N'] = 0
    
    for i, choice in enumerate(choices):
        if choice == 4:
            continue
        if choice > 4:  # 동의
            dict_score[survey[i][1]] += (choice - 4)
        else:           # 비동의
            dict_score[survey[i][0]] += (4 - choice)
    
    answer += 'R' if dict_score['R'] >= dict_score['T'] else 'T'
    answer += 'C' if dict_score['C'] >= dict_score['F'] else 'F'
    answer += 'J' if dict_score['J'] >= dict_score['M'] else 'M'
    answer += 'A' if dict_score['A'] >= dict_score['N'] else 'N'
    
    return answer