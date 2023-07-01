# matplotlib
import matplotlib.pyplot as plt
'''
# 우리나라 연간 1인당 국민소득 시각화
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [67.0, 80.0, 257.0, 1686.0, 6505, 11865.0, 22105.3]
plt.plot(years, gdp, color='green', marker='o', linestyle='dotted')
plt.title("GDP per capita")
plt.ylabel("dollars")
plt.savefig("gdp_per_capita.png", dpi=600)  # png 이미지로 저장
plt.show()

# 수학함수
x = [x for x in range(-10, 10)]
y = [2*t for t in x]
plt.plot(x, y, marker='o')
plt.axis([-20,20,-20,20])
plt.show()
'''
# 3개 함수 동시에 그리기
x = [x for x in range(-10, 10)]
y1 = [2*t for t in x]
y2 = [t**2+5 for t in x]
y3 = [-t**2-5 for t in x]
plt.plot(x, y1, 'r--', x, y2, 'g^--', x, y3, 'b*:')
plt.axis([-30,30,-30,30])
plt.show()
'''
x = [x for x in range(20)]
y = [x**2 for x in range(20)]
z = [x**3 for x in range(20)]
plt.plot(x, x, label='linear')      # 각 선에 대한 레이블
plt.plot(x, y, label='quadratic')
plt.plot(x, z, label='qubic')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title('Plot')
plt.legend()
plt.show()

# 삼각함수
import math
x = []
y = []
z = []
for angle in range(360):
    x.append(angle)
    y.append(math.sin(math.radians(angle)))
    z.append(math.cos(math.radians(angle)))
plt.plot(x,y)
plt.plot(x,z,'r-')
plt.title("SINE & COSINE WAVE")
plt.show()

# 막대형 그래프
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [67.0, 80.0, 257.0, 1686.0, 6505, 11865.0, 22105.3]
plt.bar(range(len(years)), gdp)         # 가로축 범위
plt.title("GDP per capita")
plt.ylabel("dollars")
plt.xticks(range(len(years)), years)    # 가로축 범위의 눈금마다 부여할 눈금값 지정
plt.show()

# 파이 차트
times = [8,4,10,2]
timelabels = ['Sleep', 'Move', 'Study', 'Play']
plt.pie(times, labels=timelabels, autopct='%0.2f')
plt.show()
'''