# 사용자 지정 모듈
print("start:", __name__) # 이름을 가져오는 내장 변수
PI = 3.14

def add(a, b):
    return a + b
    
if __name__ == "__main__":
    print(PI)