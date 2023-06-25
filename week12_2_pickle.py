# pickle : 객체 형태 그대로 유지하여 파일에 저장, 불러옴

import pickle
f = open('C:\doit\desk.txt','wb')
data = {1:'python', 2:'you need'}
pickle.dump(data, f)
f.close()

f = open('C:\doit\desk.txt', 'rb')
data = pickle.load(f)
print(data)