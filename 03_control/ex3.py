# for문
# for (int i = 0; i < 10; i++)
# for i in iterable 객체:
for i in range(5):
    print(i,end = ' ')
print()
a = range(5)
print(a.start, a.stop, a.step)

# 1~5
for i in range(0,6):
    print(i,end = ' ')
print()
for i in range(0,10,2):
    print(i,end = ' ')
print()
# 1~10까지의 합
t = 0
for i in range(1,11):
    t += i
else:
    print(f"{t}")
print(sum(range(1,11)))
s = "hi12!@찍찍🐀🤮"
for c in s:
    print(c,end = " ")
print()
print(len(s))
for i in range(2,10):
    for z in range(1,10):
        print(f"{i} x {z} = {i*z:<5d}",end = ' ')
    print()