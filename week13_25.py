# 파이썬 실력 키우기 2
'''
# 탭을 공백 4개로 바꾸기
import sys
src = sys.argv[1]
dst = sys.argv[2]

f = open(src)
tab_content = f.read()
f.close()
space_content = tab_content.replace('\t',' '*4)

# b.txt에 저장할 수 있도록 프로그램 수정
f = open(dst, 'w')
f.write(space_content)
f.close()
'''

# sub_dir_search : 하위 디렉토리 검색하는 프로그램
import os
def search(dirname):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            # 디렉토리인지 파일인지 구별
            if os.path.isdir(full_filename):
                search(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]
                if ext == '.py':
                    print(full_filename)
    except PermissionError:
        pass
search("C:/")

# os.walk : 하위 디렉토리 쉽게 검색
import os
for (path, dir, files) in os.walk("c:/"):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == '.py':
            print("%s%s" %(path,filename))