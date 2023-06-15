# 함수의 매개변수 *args 이해
def add_many(*args):
    result = 0  # 변수 result 초기화
    for i in args:
        result += i
    return result
result = add_many(1,2,3)
print(result)
result = add_many(1,2,3,4,5,6,7,8,9,10)
print(result)

# 매개변수가 있는 *args, add_mul()
def add_mul(choice, *args):
    if choice == 'add':
        result = 0
        for i in args:
            result += i
    elif choice == 'mul':
        result = 1
        for i in args:
            result *= i
    return result
result = add_mul('add', 1,2,3,4,5)
print('add =', result)
result = add_mul('mul', 1,2,3,4,5)
print('mul =', result)