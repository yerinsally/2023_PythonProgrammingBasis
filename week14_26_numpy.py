# numpy
import numpy as np

mid_scores = np.array([10, 20, 30])
final_scores = np.array([60, 70, 80])
total = mid_scores + final_scores
print('시험성적의 합 :', total)

# 도전문제
a = np.array(range(1,11) + np.array(range(1,101,10)))
print(a.ndim)   # 배열의 축, 차원
print(a.shape)  # 배열 차원의 원소 개수
print(a.size)   # 배열 원소의 개수
print(a.dtype)  # 넘파이 자체 자료형
print(a.data)   # 실제 원소를 포함하고 있는 주소

# 다차원 배열
array_a = np.array([0,1,2,3,4,5,6,7,8,9])
array_b = np.array(range(10))
array_c = np.array(range(0,10,2))
print('array_a =', array_a)
print('array_b =', array_b)
print('array_c =', array_c)
print('array_c의 shape', array_c.shape)
print('array_c의 ndim', array_c.ndim)
print('array_c의 dtype', array_c.dtype)
print('array_c의 size', array_c.size)
print('array_c의 itemsize', array_c.itemsize)

# 월급
salary = np.array([220,250,230])
salary = salary * 2.1
print(salary)

# 화씨온도 -> 섭씨온도 변환
ftemp = [63, 73, 80, 86, 84, 78, 66, 54, 45, 63]
F = np.array(ftemp)
print(F)
C = (F-32)*5/9
print('섭씨온도 :', C)
C_list = [(n-32)*5/9 for n in ftemp]    # 리스트로 작성
print('섭씨온도 리스트 :', C_list)

# BMI 계산
heights = [1.83, 1.76, 1.69, 1.86, 1.77, 1.73, 1.65]
weights = [86, 74, 59, 95, 80, 68, 57]
np_heights = np.array(heights)
np_weights = np.array(weights)
bmi = np_weights/(np_heights**2)
print('BMI 지수 :', bmi)
print(bmi[bmi > 25])    # BMI 25 넘는 사람들만 출력

# 인덱싱, 슬라이싱
scores = np.array([88, 72, 93, 94, 89, 78, 99])
print(scores[1:4])
print(scores[3:])
print(scores[4:-1])

# 2차원 배열
x = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(x[0][2])
print(x[0, 2])
y = np.array([['a','b','c','d'],
              ['c','c','g','h']])
print(y[y == 'c'])
