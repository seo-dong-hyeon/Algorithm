def solution(N, stages):
    answer = []
    user_cnt = len(stages)      # 스테이지에 도달한 플레이어 수(기본값 = 전체 플레이어 수)
    stage_cnt = [0] * (N + 2)   # i번 스테이지에 도전중인 플레이어 수
    dic_failrate = {}           # 실패율

    stages.sort()
    for stage in stages:
        stage_cnt[stage] += 1

    # 매 스테이지를 기준으로
    for i in range(1, N + 1):
        # 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
        dic_failrate[i] = stage_cnt[i] / user_cnt if stage_cnt[i] != 0 else 0
        # 현재 플레이어 수 갱신(해당 스테이지를 아직 클리어하지 못한 플레이어 수 제거)
        user_cnt -= stage_cnt[i]

    # 실패율 기준 정렬
    for stage, failRate in sorted(dic_failrate.items(), key=lambda x : x[1], reverse=True):
        answer.append(stage)

    return answer