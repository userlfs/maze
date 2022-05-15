import random
l = int(input("输入迷宫大小："))  # 横纵有多少条路
listl = l * 2 + 1  # 列表宽度（二维）
p = []  # 迷宫
a = 2  # 墙
b = 1  #路（待回溯）
c = " "  #路（最终的）
x, y = 1, 1 # 开始位置，y：从上到下，x：从左到右
def printlist(double_list): # 打印列表
     for i in range(len(double_list)):
         for j in double_list[i]:
             print(j,end=' ')
         print()
for i in range(listl):  # 创建二维列表
    p.append([])
    for i1 in range(listl):
            p[i].append(a)
def a1(): # 检测是否可以开路（1能/0不能）
    if y > 1:
        if  p[y-2][x] == a:
            return 1
    if x > 1:
        if  p[y][x-2] == a:
            return 1
    if y < listl - 2:
        if  p[y+2][x] == a:
            return 1
    if x < listl - 2:
        if  p[y][x+2] == a:
            return 1
    return 0
def a2(): # 检测是否可以回溯（1能/0不能）
    aa, bb = 0, 0
    if y > 1:
        aa = aa + 1
        if  p[y-2][x] != a:
            bb = bb + 1
    if x > 1:
        aa = aa + 1
        if  p[y][x-2] != a:
            bb = bb + 1
    if y < listl - 2:
        aa = aa + 1
        if  p[y+2][x] != a:
            bb = bb + 1
    if x < listl - 2:
        aa = aa + 1
        if  p[y][x+2] != a:
            bb = bb + 1
    if aa == bb:
        return 1
    else:
        return 0
i2 = 1
while i2 == 1: # 生成迷宫
    if a1() == 1:
        i = 1
    if a2() == 1: # 回溯
        i = 0
        if p[y-1][x] == b: # 上
            p[y][x], p[y-1][x] = c, c
            y = y - 2
        elif p[y+1][x] == 1: # 下
            p[y][x], p[y+1][x] = c, c
            y = y + 2
        elif p[y][x-1] == 1: # 左
            p[y][x], p[y][x-1] = c, c
            x = x - 2
        elif p[y][x+1] == 1: # 右
            p[y][x], p[y][x+1] = c, c
            x = x + 2
    while i == 1: # 开路
        d = random.randint(1,4)
        if y > 1 and d == 1 and p[y-2][x] == a: # 上
            p[y][x], p[y-1][x] = b, b
            y, i = y - 2, 0
        elif y < listl - 2 and d == 2 and p[y+2][x] == a: # 下
            p[y][x], p[y+1][x] = b, b
            y, i = y + 2, 0
        elif x > 1 and d == 3 and p[y][x-2] == a : # 左
            p[y][x], p[y][x-1] = b, b
            x, i = x - 2, 0
        elif x < listl - 2 and d == 4 and p[y][x+2] == a: # 右
            p[y][x], p[y][x+1] = b, b
            x, i = x + 2, 0
    if y == 1 and x == 1:
        i2 = 0
        p[y][x] = c
    printlist(p)
    print(y, ",", x, "↑")