# imos 알고리즘

def solution(menu, order, k):
    answer = 0

    imos = [0] * 1000001
    s = 0
    e = 0
    for i in range(len(order)):
        s = i * k
        # 새 손님이 들어와서 주문을 한 시간과
        # 이전 손님 주문이 끝나고 새 주문을 끝낸 시간 중
        # 더 큰 쪽이 진짜 끝낸 시간
        e = max(e + menu[order[i]], s + menu[order[i]])
        # 입장과 퇴장만 기록
        imos[s] += 1
        imos[e] -= 1

    now = 0
    for i in range(len(imos)):
        now += imos[i]
        imos[i] = now

    answer = max(imos)

    return answer
