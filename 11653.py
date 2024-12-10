def prime_factorization(N):
    factor = 2
    while factor * factor <= N:
        while N % factor == 0:
            print(factor)
            N //= factor
        factor += 1
    if N > 1:  # 마지막으로 남은 소수가 있을 경우 출력
        print(N)

# 입력 및 실행
N = int(input())
if N > 1:
    prime_factorization(N)
