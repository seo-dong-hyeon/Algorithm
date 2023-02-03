# imos 알고리즘

def get_time(time):
    hours, minutes = map(int, time.split(':'))
    return hours * 60 + minutes


# 입장(s)과 퇴장(e)만 기록
def solution(book_time):
    answer = 0
    end_time = 24 * 60
    prefix_sum = [0] * (end_time + 100)

    for start_time, end_time in book_time:
        start_time = get_time(start_time)
        end_time = get_time(end_time) + 10 # 청소시간 포함
        prefix_sum[start_time] += 1
        prefix_sum[end_time] -= 1

    # 한 번에 쓸면서 누적합 계산
    for i in range(len(prefix_sum) - 1):
        prefix_sum[i + 1] += prefix_sum[i] 

    answer = max(prefix_sum)

    return answer


print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))