# 간단한 메모장
'''
# sys.argv 입력된 값을 읽어들이기
import sys
option = sys.argv[1]
memo = sys.argv[2]
'''
# memo 추가, 읽기
import sys
option = sys.argv[1]

if option == '-a':
    memo = sys.argv[2]
    f = open('C:/Python/PythonProgrammingBasis/week13/memo.txt','a')
    f.write(memo)
    f.write('\n')
    f.close()
elif option == '-v':
    f = open('memo.txt')
    memo = f.read()
    f.close()
    print(memo)
