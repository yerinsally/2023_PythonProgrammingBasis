# while문 예제
'''
treeHit = 0
while treeHit < 10:
    treeHit = treeHit + 1
    print('나무를 %d번 찍었습니다.' %treeHit)
    if treeHit == 10:
        print('나무 넘어갑니다.')

# break문 : 커피자판기 예제
coffee = 10
money = 30
while money:
    print('커피 서비스')
    coffee -= 1
    print('남은 커피의 양은 %d개' %coffee)
    if coffee == 0:
        print('커피가 다 떨어졌습니다. 판매를 중지합니다.')
        break
'''
# 실제 동작 과정과 유사한 커피자판기 실습
coffee = 10
while True:
    money = int(input('돈 입력 : '))
    if money == 300:
        print('커피를 줍니다.')
        coffee -= 1
    elif money > 300:
        print('거스름돈 %d를 주고 커피를 줍니다.' %(money - 300))
        coffee -= 1
    else:
        print('돈을 다시 돌려주고 커피를 주지 않습니다.')
        print('남은 커피의 양은 %d개입니다.' %coffee)
    if coffee == 0:
        print('커피가 다 떨어졌습니다. 판매를 중지합니다.')
        break