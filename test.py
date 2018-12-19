import sys
sys.stdin = open('input.txt')

islist = []
while True:
    inp = input().split(':')
    if len(inp) == 1:
        break
    islist.append(inp)
islist.sort()
flag = True
for is_ in islist:
    if int(inp[0]) % int(is_[0]) == 0:
        print(is_[1], end='')
        flag = False
if flag:
    print(inp[0])
