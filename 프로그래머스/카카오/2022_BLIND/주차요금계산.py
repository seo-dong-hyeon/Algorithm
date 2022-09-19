from math import ceil

def solution(fees, records):
    answer = []
    dic_intime = {}
    dic_staytime = {}

    for record in records:
        time, num, io = record.split()
        m, s = map(int, time.split(':'))
        time = m * 60 + s
        num = int(num)
        if io == "IN":
            dic_intime[num] = time
        else:
            dic_staytime[num] = dic_staytime.get(num, 0) + time - dic_intime[num]
            dic_intime[num] = -1

    time = (23 * 60) + 59
    for num, intime in dic_intime.items():
        if intime != -1:
            dic_staytime[num] = dic_staytime.get(num, 0) + time - dic_intime[num]

    dic_staytime = sorted(dic_staytime.items())
    for num, staytime in dic_staytime:
        staytime -= fees[0]
        answer.append(fees[1] + (ceil(staytime / fees[2]) * fees[3] if staytime > 0 else 0))

    return answer