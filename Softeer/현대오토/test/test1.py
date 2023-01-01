def solution(votes, k):
    answer = '' # 정답 : 마지막으로 탈락하는 자동차 이름
    names = set(votes) # 이름 집합 : unique한 자동차 이름
    dic = {} 

    # dic = { 자동차이름1: 득표수, 자동차이름2: 득표수,... }와 같은 딕셔너리 형태로 저장
    # dic = {'RAIN': 2, 'AVANT': 3, 'SOULFUL': 1, 'MONSTER': 2, 'SONATE': 4, 'SANTA': 1, 'GRAND': 2, 'PRIDO': 1}
    for name in names:
        dic[name] = votes.count(name) 
    
    # dic_list = [[자동차이름1, 득표수], [자동차이름2, 득표수],...]와 같은 리스트 형태로 저장
    # dic_list = [['RAIN', 2], ['AVANT', 3], ['SOULFUL', 1], ['MONSTER', 2], ['SONATE', 4], ['SANTA', 1], ['GRAND', 2], ['PRIDO', 1]]
    dic_list = []
    for key in dic.keys():
        dic_list.append([key, dic[key]]) 

    # 리스트 정렬 -> 득표수 오름차순, 득표수가 같으면 알파벳 사전 역순으로 (lambda는 인터넷에서 보는게 빠를듯)
    # dic_list = [['SOULFUL', 1], ['SANTA', 1], ['PRIDO', 1], ['RAIN', 2], ['MONSTER', 2], ['GRAND', 2], ['AVANT', 3], ['SONATE', 4]]
    dic_list.sort(key = lambda x : (-x[1], x[0]),reverse=True)
    print(dic_list)

    # kScore = 상위 k등까지의 자동차 득표수 합을 구함
    # kScore = ['SONATE', 4] + ['AVANT', 3] = 7
    kScore = 0 
    for i in range(k):
        kScore += dic_list[len(dic_list) - i - 1][1] 
    
    lastName = dic_list[0][0] # 우선 첫번째 자동차 이름을 마지막 탈락 자동차로 지정
    totalScore = 0 # 득표수가 적은 자동차들의 득표수 합

    # 득표수가 적은 자동차들의 득표수 합이 상위 k등까지의 자동차 득표수 합보다 작을때까지 진행
    # ['SOULFUL', 1] + ['SANTA', 1] + ['PRIDO', 1] + ['RAIN', 2] <= 7
    # 마지막 탈락 = RAIN
    for i in range(len(dic_list)):
        if totalScore + dic_list[i][1] < kScore: 
            lastName = dic_list[i][0] # 마지막으로 탈락하는 자동차 이름 갱신
            totalScore += dic_list[i][1] # 득표수 합 갱신
        else: 
            break
    
    answer = lastName # 최종적으로 탈락하는 자동차 이름 저장

    return answer

if __name__ == "__main__": 
    votes = ["AVANT", "PRIDO", "SONATE", "RAIN", "MONSTER", "GRAND", "SONATE", "AVANT", "SONATE", "RAIN", "MONSTER", "GRAND", "SONATE", "SOULFUL", "AVANT", "SANTA"]
    k = 2
    print(solution(votes, k))