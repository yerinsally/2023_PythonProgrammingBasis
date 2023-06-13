# 논리연산자 : 택시예제
money = int(input('돈 입력 : '))
card = True
if money >= 3000 or card:
    print('택시를 타고 가라')
else:
    print('걸어가라')

# x in s : 택시예제
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print('택시를 타고 가라')
else:
    print('걸어가라')

# 조건부 표현식
score = int(input('점수 입력 : '))
if score >= 60:
    message = 'success'
else:
    message = 'failure'
print(message)

message = 'success' if score >= 60 else 'failure'
print(message)

# 실습 예제2
fruit = 'apple'
if fruit == 'Apple':
    fruit = 'Apple'
elif fruit == 'fruit':
    fruit = 'fruit'
else:
    fruit = fruit
print(fruit)

# 실습 예제3
myage = int(input('Tell me your age? : '))
if myage <= 30:
    print('Welcome to the Club')
else:
    print('Oh! No. You are not accepted.')
print('Welcome to the Club') if myage <= 30 else print('Oh! No. You are not accepted.')