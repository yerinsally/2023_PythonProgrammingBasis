# 내장 함수

# all, any
print(all([1,2,3]))
print(all([1,2,3,0]))
print(any([1,2,3,0]))

# chr : ASCII 코드 입력받음
print(chr(97))

# dir
print(dir([]))
print(dir({1:'a'}))

# divmod
print(divmod(7,3))

# enumerate : 열거자료형
for i, name in enumerate(['body','foo','bar']):
    print(i, name)
for i, sns in enumerate(['kakao','naver','google']):
    print(i, sns)

# eval : 문자열 형태로 입력받음
print(eval('1+2'))
print(eval("'hi'+'a'"))
print(eval('divmod(4,3)'))

# filter
def positive(k):
    result = []
    for i in k:
        if i > 0:
            result.append(i)
    return result
print(positive([1,-3,2,0,-5,6]))
# filter 함수로 간단하게 표현
def positive(k):
    return k > 0
print(list(filter(positive, [1,-3,2,0,-5,6])))
# lambda로 더 간단하게 표현
print(list(filter(lambda x : x > 0, [1,-3,2,0,-5,6])))

# int
print(int('3'))
print(int(3.4))
print(int('11', 2)) # 2진수 11이 십진수로 얼마?
# 00:0, 01:1, 11:3, 100:4, 101:5 ...
print(int('1A', 16))

# isinstance
class Cooki:
    pass
a = Cooki()
b = 3
print(isinstance(a,Cooki))  # a가 Cooki의 객체?
print(isinstance(b,Cooki))

# map
def two_time(numlist):
    result = []
    for num in numlist:
        result.append(num*2)
    return result
print(two_time([1,2,3,4]))
# map 함수로 간단하게
def two_times(x):
    return x*2
print(list(map(two_times, [1,2,3,4])))
# lambda로 더 간단하게 표현
print(list(map(lambda x : x*2, [1,2,3,4])))

# oct : 정수를 8진수 문자열로 반환
print(oct(34))
print(oct(12345))

# ord : ASCII 코드 반환
print(ord('a'))
print(ord('0'))

# pow : 제곱
print(pow(2,4))
print(pow(3,3))

# range
print(list(range(5)))
print(list(range(5,10)))
print(list(range(1,10,2)))
print(list(range(0,-10,-1)))

# round
x = [1.5, 2.5, -1.5, -2.5]  # round 적용하면 2,3,-1,-2
print(round(x[0]), round(x[1]), round(x[2]), round(x[3]))   # 2,2,-2,-2
# x >= 0 : 홀수이면 올림, 짝수이면 내림
# x < 0 : 홀수이면 내림, 짝수이면 올림

# sorted
print(sorted([3,1,2]))
print(sorted('zero'))

# str, sum
print(sum([1,2,3]))
print(sum([4,5,6]))

# zip
print(list(zip([1,2,3], [4,5,6])))
print(list(zip([1,2,3],[4,5,6],[7,8,9])))
print(list(zip('abc','def')))

# 연습문제
print(all([1, 2, abs(-3)-3]))   # False
print(chr(ord('a')) == 'a')     # True
print(list(filter(lambda x : x > 0, [1,-2,3,-5,8,-3])))
print(hex(234))     # 10진수를 16진수로 표현
print(int('0xea', 16))
print(list(map(lambda x : x*3, [1,2,3,4])))
a = [-8,2,7,5,-3,5,0,1]
print((max(a) + min(a)))
print(round(17/3, 4))