# 반복연습
print('='*20)
print('My Program')
print('='*20)

# 문자열 길이 구하기
a = "Life is too short, You need Python"
print(len(a))

# 문자열 인덱싱
a = "Life if too short, You need Python"
print(len(a))
print(a[3])
print(a[0])
print(a[33])
print(a[-1])
print(a[-6])
print(a[-0])
print(a[0] + a[1] + a[2] + a[3])

# 문자열 슬라이싱
# 슬라이싱 시 끝 인덱스는 포함되지 않음
print(a[0:5])
print(a[0:3])
print(a[12:17])
print(a[19:])
print(a[:17])
print(a[19:-7])

# 문자열의 요소값은 바꿀 수 없다 : immutable 자료형
a = "Pithon"
print(a[:1])
print(a[2:])
print(a[:1] + 'y' + a[2:])
