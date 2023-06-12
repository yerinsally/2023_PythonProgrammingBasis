# 리스트 관련 함수

# append()
a = [1,2,3]
a.append(4)
print(a)

# sort()
a = [1,4,2,3]
a.sort()
print(a)

# reverse()
a = ['a','c','b']
a.reverse()
print(a)

# index()
a = [1,2,3,4,5]
b = a.index(3)
print(b)
print(a.index(1))

# remove()
a = [1,2,3,1,2,3]
a.remove(3)
print(a)

# pop()
a = [1,2,3]
a.pop(1)    # 위치값
print(a)

# count()
a = [1,2,3,1]
b = a.count(1)
print(b)

# extend()
a = [1,2,3]
a.extend([4,5])
print(a)


# Q1
pin = '881120-1068234'
ymd = pin[:6]
num = pin[7:]
print('연월일:', ymd)
print('번호:', num)

# Q2
sex = pin[7]
print('성별:', sex)

# Q3
a = 'a:b:c:d'
b = a.replace(':','#')
print(b)

# Q4
a = [1,3,5,4,2]
a.sort()
a.reverse()
print(a)

# Q5
a = ['Life','is','too','short']
b = " ".join(a)
print(b)