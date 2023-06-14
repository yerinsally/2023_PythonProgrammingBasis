# for문 응용
'''
marks = [90,25,67,45,80]
number = 0
for mark in marks:
    number += 1
    if mark >= 60:
        print('{0}번 학생은 합격입니다.'.format(number))
    else:
        print('{0}번 학생은 불합격입니다.'.format(number))

marks = [90,25,67,45,80]
number = 0
for mark in marks:
    number += 1
    if mark < 60:
        continue    # 불합격이면 출력하지 않음
    else:
        print('{0}번 학생은 합격입니다.'.format(number))

# for문 range함수 사용
add = 0
for i in range(1,11):
    add += i
print('1부터 10까지 총합 :', add)

# range 함수 사용 예제
marks = [90,25,67,45,80]
for number in range(len(marks)):
    if marks[number] < 60:
        continue
    else:
        print('%d번 학생 축하합니다. 합격입니다.' %(number+1))

# 터틀그래픽 : for, range로 회오리 그리기
import turtle as t
t.shape('turtle')
t.color('blue')
t.speed(0)
angle = 91
for x in range(200):    # 사각형이 커지면서 회전
    t.fd(x)
    t.left(angle)
t.hideturtle()
t.exitonclick()
'''
# 구구단 출력 : 이중 중첩 for 루프 사용
for i in range(2, 10):
    for j in range(1, 10):
        print(i*j, end=' ')     # 가로 출력, 한칸 띄기
    print('')