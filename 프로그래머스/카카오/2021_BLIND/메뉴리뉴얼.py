from itertools import combinations

def solution(orders, course):
    answer = []

    # 주문 내역 정렬
    order_list = [[] for _ in range(len(orders))]
    for i, order in enumerate(orders):
        for j in range(len(order)):
            order_list[i].append(order[j])
        order_list[i].sort()

    for i in range(len(course)):
        dict_menu = {}
        for order in order_list:
            # 주문 내역중에서 코스 개수에 맞는 조합 생성
            for nCr in list(combinations(order, course[i])):
                if nCr not in dict_menu:
                    dict_menu[nCr] = 0
                dict_menu[nCr] += 1
        # 최소 2개 이상의 주문을 하면서 가장 많이 주문한 조합 선택
        cnt = 2
        for menu in sorted(dict_menu.items(), key=lambda x:-x[1]):
            if menu[1] >= cnt:
                cnt = menu[1]
                answer.append("".join(list(menu[0])))
            else:
                break

    answer.sort()

    return answer