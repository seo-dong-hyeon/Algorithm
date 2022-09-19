def solution(id_list, report, k):
    answer = []
    dic_cnt_reported = {}
    dic_report = {}

    for r in report:
        reporter, reported = r.split()
        if reporter not in dic_report:
            dic_report[reporter] = set()
        if reported not in dic_report[reporter]:
            dic_report[reporter].add(reported)
            dic_cnt_reported[reported] = dic_cnt_reported.get(reported, 0) + 1

    for id in id_list:
        result = 0
        reported_list = list(dic_report[id]) if id in dic_report else []
        for reported in reported_list:
            if dic_cnt_reported[reported] >= k:
                result += 1
        answer.append(result)

    return answer