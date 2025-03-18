# 조건
# 첫째 줄에 n이 주어진다. n은 10,000보다 작거나 같은 자연수 또는 0이다.

# 재귀 함수 기반 함수 문제 풀이
# 런타임 에러 (RecursionError)
# def fibo(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibo(n-1) + fibo(n-2)
#
# input_num = int(input())
# print(fibo(input_num))

# 위 코드는 입력값 n이 클 경우 중복 계산이 많아지고,
# 재귀 호출의 깊이가 깊어져 RecursionError가 발생할 수 있음

# 해결 방법
# 반복문 기반 피보나치 함수 문제 풀이
def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b

    return b

input_num = int(input())
print(fibo(input_num))