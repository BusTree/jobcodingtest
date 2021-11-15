from collections import deque

# def bfs(graph, start, visited):
#     queue = deque([start])
#     # 큐에서 하나의 원소를 뽑아 출력
#     while queue:
#         v = queue.popleft()
#         print(v, end='')
#
#         # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
#         for i in graph[v]:
#             if not  visited[i]:
#                 print('통과가능')
#                 queue.append(i)
#                 visited[i] = True

input_list = [
    [],
    [1, 0, 1, 0, 1, 0],
    [1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1]
]

visited = [False] * len(input_list)

def escape(graph, start, visited):
    queue = deque([start])

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


result = escape(input_list, 1, visited)
print('result')
print(result)

# 다시 풀어볼 것
# 노드가 1일경우 최단거리 기록 후 add하는 방식인데
# 노드가 여러방향에있을때 어떻게 기록하는지 궁금 
# 노트에 그려가면서 이해해볼것