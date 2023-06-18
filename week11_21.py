# try, except 문
a = [1,2]
try:
    a[3]
except IndexError as e:
    print(e)

# try ~ finally 문
a = [1,2]
try:
    a[3]
    f = open('C:/doit/foo.txt','w')
    data = ('우리는 try~finally문을 학습하고 있습니다.')
    f.write(data)
    f.close()
except IndexError as e:
    print(e)
finally:
    f = open('C:/doit/foo.txt','r')
    data = f.read()
    print(data)
    f.close()       # finally절 : try문 수행 중 예외 발생여부에 상관없이 항상 수행됨

# 여러 개의 오류 처리하기
try:
    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except IndexError:
    print('인덱싱할 수 없습니다.')   # ZeroDivisionError 오류는 발생 안함

try:
    a = [1,2]
    print(a[3])
    4/0
except(ZeroDivisionError, IndexError) as e:   # 오류 함께 처리
    print(e)    # list index out of range 발생

# 오류 회피하기 : pass
try:
    f = open('C:/doit/나없는파일.txt','r')
except FileNotFoundError:
    pass

# 오류 일부러 발생시키기 : raise
# Bird클래스 상속받는 클래스는 반드시 fly 함수 구현하도록 함
class Bird:
    def fly(self):
        raise NotImplementedError
'''
class Eagle(Bird):
    pass
eagle = Eagle()
print(eagle.fly())  # fly 함수 X, NotImplementError 발샏
'''
# NotImplemetedError 발생되지 않게 : Eagle 클래스에 fly 함수 구현
class Eagle(Bird):
    def fly(self):
        print('very fast')
eagle = Eagle()
eagle.fly()

# 예외 만들기 : 내장클래스 Exception 사용
class MyError(Exception):
    pass

def say_nick(nick):     # 별명 출력 함수
    if nick == '바보':
        raise MyError()
    print(nick)
#print(say_nick('천사'))
#print(say_nick('바보'))  # MyError 발생

# 예외처리 기법 사용하여 MyError 발생 예외처리
try:
    say_nick('천사')
    say_nick('바보')
except MyError:
    print('허용되지 않은 별명입니다.')

try:
    say_nick('천사')
    say_nick('바보')
except MyError as e:
    print(e)    # 오류 메시지 출력 X

# print(e)에 오류 보이게 하려면 __str__ 메서드 구현
class MyError(Exception):
    def __str__(self):
        return '허용되지 않은 별명입니다.'

def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)
try:
    say_nick('천사')
    say_nick('바보')
except MyError as e:
    print(e)    # 오류 메시지 출력됨