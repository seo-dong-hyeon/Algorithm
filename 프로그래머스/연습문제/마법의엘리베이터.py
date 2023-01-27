def move(storey, now, buttons):
    min_diff = 1e10
    max_button = 1
    
    # 모든 버튼을 누르면서
    # 가장 목표점에 가깝게 도달할 때의
    # 목표점과의 거리와 누른 버튼을 구함
    for button in buttons:
        next = now + button
        if next < 0 or next > 100000000:
            break
        diff = abs(storey - next)
        if min_diff > diff:
            min_diff = diff
            max_button = button
        else:
            break

    return min_diff, max_button


def solution(storey):
    answer = 0
    # 올라가는 버튼
    buttons_plus = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000]
    # 내려가는 버튼
    buttons_minus = [-e for e in buttons_plus]
    # 0층에서 시작
    now = 0

    while True:
        # 올라가는 버튼으로 가장 목표점에 가깝게 가는 경우
        min_diff_plus, max_button_plus = move(storey, now, buttons_plus)
        # 내려가는 버튼으로 가장 목표점에 가깝게 가는 경우
        min_diff_minus, max_button_minus = move(storey, now, buttons_minus)
        # 둘 중 더 목표점에 가깝게 가는 경우를 선택
        now += (max_button_minus if min_diff_plus > min_diff_minus else max_button_plus)
        answer += 1
        # 목표점에 도달했으면 종료
        if now == storey:
            break

    return answer
