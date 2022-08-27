import sys
import heapq

N = int(input())
heap = []

for i in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)
    else:
        heapq.heappush(heap, (-num, num))