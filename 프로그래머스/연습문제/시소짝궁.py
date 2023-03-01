def solution(weights):
    answer = 0

    weights_dict = {}
    for weight in weights:
        if weight not in weights_dict:
            weights_dict[weight] = 0
        weights_dict[weight] += 1

    # 같은 무게를 가진 애들끼리
    for weight, cnt in weights_dict.items():
        if cnt >= 2:
            answer += (cnt * (cnt - 1)) // 2

    # 시소에 앉는 위치별로 나올 수 있는 가중치
    distances = [(2, 3), (2, 4), (3, 2), (3, 4), (4, 2), (4, 3)]
    for weight in weights_dict.keys():
        for dist1, dist2 in distances:
            friend_weight = weight * dist1 / dist2
            if friend_weight in weights_dict:
                answer += weights_dict[weight] * weights_dict[friend_weight]
        # 이미 계산을 끝낸 몸무게는 중복 계산이 되지 않도록 제거
        weights_dict[weight] = 0

    return answer
