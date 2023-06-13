# 첫번째 예제
'''money = int(input('돈 입력 : '))
if money >= 3000:
    print('택시를 타고 가라')
else:
    print('걸어가라')'''

# 동전 던지기 게임
import random
print('동전 던지기 게입을 합니다.')
coin = random.randrange(2)      # 0 또는 1
print(coin)
if coin == 1:
    print('앞면입니다.')
else:
    print('뒷면입니다.')
print('게임이 종료되었습니다.')