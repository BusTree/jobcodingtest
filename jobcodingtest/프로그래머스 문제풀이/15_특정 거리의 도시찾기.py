# 특정 거리의 도시찾기 DFS/BFS 문제
# n = 도시의 개수
# m = 도로의 개수
# k = 거리정보
# x = 출발 도시의 번호

from collections import deque

# loadMap = [[], [1, 2], [1, 3], [2, 3], [2, 4]]
# graph = [[], [2, 3], [3, 4], [], []]

loadMap = [[], [1, 2], [1, 3], [2, 3], [2, 4]]
graph = [[], [2, 3], [3, 4], [], []]
visited = [False] * 9

# BFS 메서드 정의
def bfs(graph, start, visited, count):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        count += 1
        # 큐에서 하나의 원소를 뽑아 출력
        print(queue)
        v = queue.popleft()
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True



            if count == 2 and i == len(graph[v]) - 1:
                print('stop')
                print(queue)
                return queue

result = bfs(graph, 1, visited, 0)
print('result')
print(result)


def solution(n, m, k, x):
    for i in graph[x]:
        for j in i:
            print()

    return 0

bb = []
def search(graph, x):
    bb.append(graph[x])
    for i in graph[x]:
        search(graph, i)

result = search(graph, 1)
print('bb')
print(bb)
# result = solution(4, 4, 2, 1)
