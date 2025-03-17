# https://www.acmicpc.net/problem/10828

# 문제 분석
# 정수를 저장하는 스택을 구현합니다.
# 총 다섯 가지의 명령을 구현합니다.

# 해결 방법
# 1. push X: 정수 X를 스택에 넣는 연산이다.
# 2. pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# 3. size: 스택에 들어있는 정수의 개수를 출력한다.
# 4. empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# 5. top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

# 알고리즘
# 주어지는 명령의 수와 명령을 차례대로 수행 후 결과를 한 줄에 하나씩 출력합니다.
# 클래스로 Stack을 구현하여 코드의 가독성과, 유지보수성, 확장성을 높입니다.

# 코드 가독성 향상 -> Stack 객체를 통해 스택 기능을 직관적으로 사용 가능
# 유지보수성 증가 -> 수정해야 할 기능이 많아도 한 곳(Stack 클래스)에서 관리 가능
# 재사용성 증가 -> 다른 문제에서도 쉽게 Stack 클래스를 재사용 가능
# 확장성 증가 -> 추가적인 기능 (get_max, get_min 등) 을 쉽게 추가 가능
# OOP 원칙 준수 -> 캡슐화를 활용하여 데이터 보호 가능

# 시간 복잡도
# O(1)

import sys
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, X):
        self.stack.append(X)

    def pop(self):
        if self.is_empty():
            return -1
        return self.stack.pop()

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return 1 if not self.stack else 0

    def top(self):
        if self.is_empty():
            return -1
        return self.stack[-1]

def process_commands(commands):
    stack = Stack()
    result = []

    for command in commands:
        if command.startswith("push"):
            _, X = command.split()
            stack.push(int(X))
        elif command == "pop":
            result.append(stack.pop())
        elif command == "size":
            result.append(stack.size())
        elif command == "empty":
            result.append(stack.is_empty())
        elif command == "top":
            result.append(stack.top())

    return result

data = sys.stdin.readlines()  # 여러 줄 입력을 리스트로 읽기
n = int(data[0].strip())  # 첫 번째 줄: 명령어 개수
commands = [line.strip() for line in data[1:]]  # 명령어 리스트

# 명령어 처리 및 출력
results = process_commands(commands)
print("\n".join(map(str, results)))
