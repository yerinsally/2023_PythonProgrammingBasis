# 화씨온도를 섭씨온도로 변환
f_temp = int(input("화씨온도 입력:"))
c_temp = (f_temp-32)*5/9
print("섭씨온도:", c_temp)
print("섭씨온도:%0.2f"%c_temp) # 소수점 자리

# 섭씨온도를 화씨온도로 변환
c_temp = int(input("섭씨온도 입력:"))
f_temp = (c_temp*9/5)+32
print("화씨온도:", f_temp)