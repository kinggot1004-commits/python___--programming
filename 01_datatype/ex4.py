# 문자열(str)
# "", ''
a = "python"
print(a,type(a))
print("I'll be back")
print('I\'ll be back')
# 여러줄 문자열
a = """
Life is short
You need python
"""
print(a)
def func():
    """
    func() 함수에 대한 설명 작성
    """
    pass
print(func.__doc__)
# 문자열 연결
print('hello','python')
print('hello'*10)
print('-'*50)

print("10" + "3")
print(int("10") + int("3"))
# 문자열 포멧팅
age = 21
name = "pororo"
print(f"이름{{}}: {name}, 나이: {age}")
print(f"내년나이: {age+1}")
print(f": {name.upper()}")
pi = 3.141592
print(f"{pi:.3f}")
print(f"{pi:.0f}")
num = 123456789
print(f"{num:,}")

print(f"{num:15d}")
print(f"{num:<15,d}")

print(f"{num:015,d}")
print(f"{num:<015,d}")