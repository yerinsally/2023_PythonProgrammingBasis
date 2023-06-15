# 실습문제
# 1번
def print_school(name, school):
    print('이름:',name)
    print('학교:',school)
print_school('눈송이', '숙명여자대학교')

# 2번
def get_sum(start, end):
    sum = 0
    for i in range(start,end):
        sum += i
    return(sum)
print('start에서 end까지의 합:', get_sum(1,10))
print('start에서 end까지의 합:', get_sum(1,1000))

# 3번
def get_square(a,b,c):
    return a**2, b**2, c**2
a_sq, b_sq, c_sq = get_square(2, 5, 7)
print('2의제곱:',a_sq, ', 5의제곱:',b_sq, ', 7의제곱:',c_sq)

# random 가위바위보 맞추기
import random
computer = random.randint(0,2)
mine = input('가위,바위,보 중 하나를 입력하세요:')
gbbGames = ['가위','바위','보']
if mine == gbbGames[computer]:
    print('맞혔습니다.')
else:
    print('틀렸습니다.')
print('저는 <',gbbGames[computer],'> 였습니다.')