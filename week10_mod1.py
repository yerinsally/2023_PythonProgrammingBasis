# 모듈
# 'C:\doit\'에 있는 실습파일임

# mod1.py : 모듈 파일
def add(a,b):
    return a+b
def sub(a,b):
    return a-b

# 모듈 변경
if __name__ == "__main__":
    print(add(1,4))
    print(sub(4,2))
# 직접 이 파일을 실행 시 : __name__ == "__main__" 참
# 대화형 인터프리터 실행 시 : __name__ == "__main__" 거짓