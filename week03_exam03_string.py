# 문자열 포매팅 학습
print("I eat %d apples." %3)
print("I eat %s appples."%"five")
# 문자열은 s 삽입
#  %s 포맷 코드로 어떤 형태로든 변환 가능

number = 3
day = "three"
print("I eat %d apples." %number)
print("I ate %d apples. So I was sick %s days." %(number, day))

print("Error is %d%%" %98)


# 포맷코드와 숫자 함께 사용하기
# 정렬과 공백
print("%10s" %"hi")
print("%-10s" %"hi")
print("%-10sjane" %"hi")

# 소수점 표현하기
print("%0.4f" %3.1234567890)
print("%0.2f" %3.1234567890)
print("%.2f" %3.1234567890)
print("%10.4f" %3.1234567890) # 전체 10자리에 소숫점 4자리까지

# .format() 함수
print("I eat {} apples.".format(3))
print("I eat {} apples.".format("five"))

number = 10
day = "three"
print("I ate {} apples. So I was sick {} days.".format(number, day))
print("I ate {} apples. So I was sick {day} days.".format(3, day = "three"))

# f 문자열 포매팅
name = "눈송이"
age = 23
print(f"나의 이름은 {name}입니다. 나이는 {age}입니다.")
print(f"눈송이는 내년에 {age+1}살이 됩니다.")

# 고급 문자열 포매팅
# 1. 왼쪽 정렬
print("{0:<10}".format("hi"))
print(f'{"hi":<10}')
# 2. 오른쪽 정렬
print("{0:>10}".format("hi"))
print(f'{"hi":>10}')
# 3. 가운데 정렬
print("{0:^10}".format("hi"))
print(f'{"hi":^10}')
# 4. 공백 대신 다른 문자
print("{0:=^10}".format("hi"))
print("{0:!<10}".format("hi"))
print(f'{"hi":!<10}')

# 소수점 표현하기
y = 3.4211234234
print('{0:0.4f}'.format(y))
print(f'{y:0.4f}')

# {} 문자 표현하기
print("{{ and }}".format())
print(f'{{and}}')


# 문자열 함수
a = "hobby"
print(a.count('b'))
a = "Python is the best choice."
print(a.find('b'))
print(a.find('k'))
print(a.index('b'))
#print(a.index('k')) # Error 발생

# 문자열 삽입 join()
print(",".join("abcd"))

# 공백 지우기 (왼쪽, 오른족, 양쪽)
a = "      hi"
print(a.lstrip())
a = "hi      "
print(a.rstrip())
a = "   hi   "
print(a.strip())

# 문자열 바꾸기 : replace()
a = "Life is too short"
print(a.replace("Life", "Your leg"))