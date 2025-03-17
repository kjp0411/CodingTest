# https://www.acmicpc.net/problem/1158

# 문제 분석
# 1번부터 N번까지 사람들이 원형으로 앉아 있음.
# K번째 사람을 순서대로 제거함.
# 사람이 제거된 후, 그 다음 사람부터 다시 K번째를 세어 제거함.
# 모든 사람이 제거될 때까지 반복하며, 제거되는 순서를 출력.

# 1번부터 N번까지 원 순열을 이룸
# N이 7이고 K가 3이면
# 1, 2, 3, 4, 5, 6, 7
# Linked list로 next값 연결 or deque.rotate()로 회전시키면서 pop

# 첫번째 사라지는 원소는 3번째인 3
# 두번째 사라지는 원소는 3을 기준으로 3번째인 6
# 세번째 사라지는 원소는 6을 기준으로 3번째인 2
# 네번째 사라지는 원소는 2를 기준으로 3번째인 3과 6은 제거되었기 때문에 7
# 다섯번째 사라지는 원소는 7을 기준으로 2와 3은 제거되었기 때문에 5
# 여섯번째 사라지는 원소는 5를 기준으로 6과 7은 제거되었기 때문에 1
# 일곱번째 사라지는 원소는 1을 기준으로 4밖에 안남았기 때문에 4

# 해결 방법
# 원형 연결 리스트 (Circular Linked List)
# → 직접 원형 구조 구현하여 매번 K번째 사람을 찾아 제거

# deque 회전 방식
# → rotate()를 이용하여 K번째 사람을 앞으로 가져오고 제거

# 시간 복잡도
# Linked List	K번째까지 이동 O(K) + 삭제 O(1)	    N번 반복	    O(NK)
# deque	        rotate(K-1) → O(K) + popleft()	    N번 반복	    O(NK)

# # 연결 리스트(Linked List) 기반 요세푸스 문제 풀이
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularLinkedList:
    def __init__(self, N):
        self.head = None
        self.tail = None
        self.create_list(N)

    def create_list(self, N):
        prev_node = None
        for i in range(1, N+1):
            new_node = Node(i)
            if not self.head:
                self.head = new_node
            else:
                prev_node.next = new_node

            prev_node = new_node
        prev_node.next = self.head
        self.tail = prev_node

    def remove_kth(self, K):
        result = []
        current = self.head
        prev = self.tail

        while current.next != current:
            for _ in range(K-1):
                prev = current
                current = current.next

            result.append(current.value)
            prev.next = current.next
            current = current.next

        result.append(current.value)
        return result

def josephus(N, K):
    cll = CircularLinkedList(N)
    return cll.remove_kth(K)

N, K = map(int, input().split())
print("<"+", ".join(map(str, josephus(N, K)))+">")


# deque 기반 요세푸스 문제 풀이
from collections import deque

def josephus(N, K):
    queue = deque(range(1, N+1))        # 1부터 N까지의 숫자를 큐에 저장
    result = []

    while queue:
        queue.rotate(-(K-1))            # K-1번 왼쪽으로 회전 (즉, K번째 사람이 맨 앞에 오도록 함)
        result.append(queue.popleft())  # K번째 사람 제거

    return result

N, K = map(int, input().split())
print("<"+ ", ".join(map(str, josephus(N, K))) +">")