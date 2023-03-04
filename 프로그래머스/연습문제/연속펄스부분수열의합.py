def get_pulsed_sequence(sequence, x):
    pulsed = []
    for s in sequence:
        pulsed.append(s * x)
        x *= -1

    return pulsed


def get_max_partial_sum(sequence):
    dp = [0] * len(sequence)
    dp[0] = sequence[0]   
    
    for i in range(1, len(sequence)):
        dp[i] = max(dp[i - 1] + sequence[i], sequence[i])

    return max(dp)


def solution(sequence):
    answer = 0

    pulsed1 = get_max_partial_sum(get_pulsed_sequence(sequence, 1))
    pulsed2 = get_max_partial_sum(get_pulsed_sequence(sequence, -1))
    answer = max(pulsed1, pulsed2)

    return answer