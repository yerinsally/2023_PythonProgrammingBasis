# 연습문제

# (1) 마일 킬로미터 변환
'''miles = float(input("마일입력:"))
kms = miles * 1.6
print("%.1f 마일은 %.1f 킬로미터 입니다." %(miles, kms))
print("{0} 마일은 {1} 킬로미터 입니다.".format(miles, kms))
print(f"{miles} 마일은 {kms} 킬로미터 입니다.")'''

# (2) 시, 분, 초 계산
time = int(input("시간을 초 단위로 입력:"))
sec = time % 60
min = time // 60
hour = min // 60
min = min % 60      # 앞 min 변수의 몫
print("%d초는 %d시간 %d분 %d초 입니다." %(time, hour, min, sec))
print("{0}초는 {1}시간 {2}분 {3}초 입니다.".format(time, hour, min, sec))
print(f"{time}초는 {hour}시간 {min}분 {sec}초 입니다.")