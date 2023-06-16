# FourCal 클래스 만들기
class FourCal:
    def setdata(self,first,second):
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
'''
a = FourCal()
a.setdata(4,2)
print(a.first)
print(a.second)
b = FourCal()
b.setdata(3,7)
print(b.first)
print(b.second)

print(id(a.first))  # 주소값
print(id(b.first))  # 주소값
'''
a = FourCal()   # 객체
a.setdata(4,2)
print(a.add())
print(a.sub())
print(a.mul())
print(a.div())

b = FourCal()   # 객체
b.setdata(4,8)
print(b.add())
print(b.sub())
print(b.mul())
print(b.div())
