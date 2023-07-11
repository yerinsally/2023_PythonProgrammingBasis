# 21번

kor = int(input('국어점수(kor):'))
eng = int(input('영어점수(eng):'))
mat = int(input('수학점수(mat):'))
sum = kor + eng + mat
avg = sum / 3
print(f'눈송이 학생의 총점은 sum={sum}이며, 평균은 'f'avg={avg:0.1f}입니다.')