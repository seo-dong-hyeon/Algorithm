def solution(elements):
    answer = 0

    nums = set()
    elements.extend(elements)
    for length in range(1, len(elements) // 2 + 1):
        for idx in range(len(elements)):
            nums.add(sum(elements[idx:idx + length]))

    answer = len(nums)

    return answer