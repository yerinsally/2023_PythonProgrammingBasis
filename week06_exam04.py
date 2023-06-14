# 리스트 내포 예제
a = [1,2,3,4]
result = []
for num in a:
    result.append(num*3)
print(result)   # 4 이후엔 거짓이 되어 프린트문으로

a = [1,2,3,4]
result = [num*3 for num in a]
print(result)

result = [num*3 for num in a if num % 2 == 0]
print(result)