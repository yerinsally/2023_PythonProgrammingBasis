# time.time()
import time
print(time.time())
print(time.localtime(time.time()))  # time.time()의 실수값을 연도, 월, 일, 시분초 형태로 바꿔줌
print(time.asctime())   # 날짜, 요일, 시간 형태 값으로 반환
print(time.ctime())     # 현재시간을 돌려줌

# time.strftime
print(time.strftime('%x', time.localtime()))   # 날짜 출력
print(time.strftime('%c', time.localtime()))   # 날짜, 시간 출력

# time.sleep()
import time
for i in range(10):
    print(i, end = ' ')
    time.sleep(0.5)

# calendar()
import calendar
print(calendar.calendar(2023))
print(calendar.prcal(2023))     # 동일한 결과값
print(calendar.weekday(2023,5,23))    # 날짜에 해당하는 요일 정보
print(calendar.monthrange(2023,12))   # 2023년 12월 1일 무슨 요일, 몇 일까지?
