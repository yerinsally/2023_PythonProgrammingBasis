# Quiz 1 실습문제 코딩하기

# 실습문제1
americano_price = 2000
cafelatte_price = 3000
capucino_price = 3500
americanos = int(input('아메리카노 판매 개수: ',))
cafelattes = int(input('카페라테 판매 개수: ',))
capucinos = int(input('카푸치노 판매 개수: ',))
sales = americanos*americano_price + cafelattes*cafelatte_price + capucinos*capucino_price
print('총 매출은 ', sales, ' 원 입니다.')

# 실습문제2
weight = float(input('몸무게를 kg 단위로 입력: '),)
height = float(input('키를 미터 단위로 입력: ',))
BMI = weight / height**2
print('당신의 BMI= %.1f'%BMI)

# 실습문제3
money = int(input('투입한 돈: '),)
price = int(input('물건 값: '),)
change = money - price
print('거스름돈: {0}' .format(change))
coin500 = change//500
change = change % 500
coin100 = change//100
print('500원 동전개수: {0}' .format(coin500))
print('100원 동전개수: {0}' .format(coin100))

# 실습문제4
price = int(input('기계값 입력: '),)
used = int(input('사용 개월 수: '),)
mpay = float(price/24)
left = 24 - used
charge = mpay*left
print('매달 내는 돈: {0} 원' .format(mpay))
print('남은 약정기간: {0} 개월' .format(left))
print('위약금: {0} 원' .format(charge))

# 실습문제5
person = int(input('MT 인원수: '),)
amount = int(input('1인당 생수 개수: '),)
total_amount = person*amount
print('필요한 생수 개수: {0}' .format(total_amount))
pack = total_amount // 15
pack_price = pack*10000
bottle = total_amount % 15
bottle_price = bottle*900
total = pack_price + bottle_price
print('생수 팩 구매량: {0} , 구입가격: {1} 원' .format(pack,pack_price))
print('생수 낱개 구매량: {0} , 가격: {1} 원' .format(bottle,bottle_price))
print('생수 총 구매 비용: {0} 원' .format(total))
