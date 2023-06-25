# random()
import random
print(random.random())
print(random.randint(1,10))
data = [1,2,3,4,5]

# random.pop : 리스트 요소 중 무작위로 하나 꺼내 제거하고 값 반환
def random_pop(data):
    num = random.randint(0, len(data)-1)
    return data.pop(num)
while data:
    print(random_pop(data), end=' ')

# random_choice : 입력받은 리스트에서 무작위로 하나 선택하여 반환
def random_choice(data):
    num = random.choice(data)
    data.remove(num)
    return num
while data:
    print(random_choice(data), end=' ')

# shuffle : 무작위로 섞을때 사용하는 함수
data = [10,20,30,40,50]
random.shuffle(data)
print(data, end=' ')