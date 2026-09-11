# 반복문: while문, for문
# while문 
# 1 ~ 10까지 반복 출력
i = 0
while i < 10:
    i +=1
    print(i)
    #if i == 5:
    #    break
else:
    print("end")
# list에서 target 값 찾기
nums = [1,3,5,7,9]
target = 2
i = 0
found = False
while i < len(nums):
    if nums[i] == 2:
        print("찾기")
        found = True
        break
    i += 1
else: # if not found
    print(f"{target} not found")
i = 1
tot = 0
while i <= 10:
    if i % 2 ==0:
        tot += i
    i += 1
print(f"sum = {tot}")

def test():
    pass