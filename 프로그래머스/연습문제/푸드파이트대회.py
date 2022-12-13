def solution(food):
    answer = '0'
    
    for i in range(len(food) - 1, -1, -1):
        cnt = food[i]
        half = cnt // 2
        answer = str(i) * half + answer + str(i) * half
    
    return answer