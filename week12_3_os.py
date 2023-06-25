# os : 환경변수, 디렉토리, 파일 등 os 차원 제어 모듈

import os
print(os.environ)
print(os.environ['PATH'])

# os.chdir : 디렉토리 위치 변경
os.chdir('C:\windows')
# os.getcwd : 디렉토리 위치 돌려받기
print(os.getcwd())
# os.system : 시스템 명령어 호출하기
print(os.system("PATH"))
# os.popen : 실행한 시스템 명령어의 결과값 돌려받기
f = os.popen("dir")
print(f.read())