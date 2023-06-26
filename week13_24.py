# 파이썬 실력 키우기 1

# 구구단 프로그램
# while문
def GuGu(n):
    result = []
    i = 1
    while i < 10:
        result.append(n*i)
        i += 1
    return result
print(GuGu(2))

# for문
def GuGu(n):
    result = []
    for i in range(1,10):
        result.append(n*i)
    return result
print(GuGu(2))

# 구구단 연습 : 결과가 두 자리로 출력되게
for i in range(2,10):
    for j in range(1,10):
        print('%d * %d = %2d' %(i, j, i*j), end=' ')
    print()


# 3과 5의 배수 합하기
# while문
result = 0  # 저장할 변수 초기화
n = 0       # count 초기화
while n < 1000:
    if (n % 3 == 0) or (n % 5 == 0):
        result += n
    n += 1  # 아니면 n 하나씩 증가
print('3과 5의 배수합 :', result)

# for문
result = 0
n = 0
for n in range(1,1000):
    if (n % 3 == 0) or (n % 5 == 0):
        result += n
print('3과 5의 배수합 :', result)


# 게시판 페이징하기
def getTotalPage(m,n):
    if m % n == 0:
        return m // n
    return m // n + 1
print(getTotalPage(5,10))
print(getTotalPage(15,10))
print(getTotalPage(25,10))
print(getTotalPage(30,10))  # 나머지가 0이면 몫에 1 더하지 않기