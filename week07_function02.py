# **kwargs : 딕셔너리 자료형으로 만들어줌
def p_kwargs(**kwargs):
    print(kwargs)
p_kwargs(a=1)
p_kwargs(name='눈송이', age=24)

# 함수 빠져나올때 return
def say_nick(nick):
    if nick == '바보':
        return
    print('나의 별명은 %s입니다.' %nick)
say_nick('야호')
say_nick('바보')

# 전역변수, 지역변수 이해
a = 1
def vartest1(a):
    a += 1
vartest1(a)  # 함수 안의 a : 아무것도 없음
print(a)    # 함수 밖의 a

# return 이용하여 함수 밖 변수 변경
a = 1
def vartest2(a):
    a += 1
    return(a)
a = vartest2(a)
print(a)

# global 명령어로 함수 밖 변수 변경
a = 1
def vartest3():
    global a
    a += 1
vartest3(a)
print(a)