# 연습문제1
a = 0       # 초기화
sum = 0     # 초기화
while a < 1000:
    a = a + 1
    if a % 3 == 0:
        sum = sum + a
print('1~1000까지 3의 배수의 합 :',sum)

# 연습문제2
b = 0
while b < 10:
    b += 1
    if b % 3 == 0:
        continue
    else:
        print(b, end=' ')   # 가로출력 방법
print()     # 줄바꿈

# 연습문제3
while True:
    line = input('>')
    if line == 'quit' or line == 'exit':
        break
    else:
        print(line)

# 연습문제4
score_list = [5, 10, 15, 20, 25, 30]
sum_score = 0
i = 0
while i < len(score_list):
    if i % 2 == 0:
        sum_score += score_list[i]
    i += 1
print(sum_score)