# 파이썬 자료형
# 1. 기본 자료형: 숫자형(정수형, 실수형), 불리언, 문자열
# 2. 컬렉션 자료형: 리스트, 튜플, 딕셔너리, 집합

# 숫자형 - 정수형(int)
a = 10
print(a,type(a))

print(bin(a),oct(a),hex(a))
print(ord("A"),chr(65))
# x = 10**100
# print(x)
# a = 2**31 + 2
# print(a)
# 실수형(float)
b = 3.14
print(b,type(b))
#float의 표현 범위
# 부동 소수점 방식
# 64비트 = 부호비트(1) + 지수부(11) + 가수부(52)
import sys
print(sys.float_info.min)
print(sys.float_info.max)
print(-sys.float_info.min)
print(-sys.float_info.max)
a = 1.7e308
b = 1.8e308
print(a,b)
# 실수의 오차
print(0.1 + 0+2 == 0.3)
print(f"{0.1:.20f}")
print(f"{0.2:.20f}")
print(0.1)

# 형변환
print(float(10))
print(int(3.14))
print(float("100"))
print(float("3.14"))
print(str(10))