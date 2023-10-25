import re
n=int(input())
reg = []
for i in range(n):
    reg.append(input())

for i in reg:
    try:
        re.compile(i)
        print(True)
    except:
        print(False)