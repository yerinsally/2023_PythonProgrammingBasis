# 생성자
class FourCal:
    def __init__(self,first,second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
a = FourCal(4,2)
print(a.first)
print(a.second)
print(a.add())
print(a.div())

# 클래스의 상속
class MoreFourCal(FourCal):     # a의 b제곱 클래스
    def pow(self):
        result = self.first ** self.second
        return result
a = MoreFourCal(4,2)
print(a.add())
print(a.first)
print(a.second)
print(a.mul())
print(a.pow())

# 메서드 오버라이딩 : ZeroDivisionError 해결
class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second
a = SafeFourCal(4,0)
print(a.div())

class FailFourCal(FourCal):
    def mul(self):
        if self.second == 0:
            return 'Fail'
        else:
            return self.first * self.second
a = FailFourCal(4,0)
print(a.mul())

# 클래스 변수
class Family:
    lastname = "김"
print(Family.lastname)  # lastname = 클래스변수
a = Family()
b = Family()
print(a.lastname)
print(b.lastname)

Family.lastname = "박"
print(a.lastname)
print(b.lastname)   # 클래스변수 공유되고 있음