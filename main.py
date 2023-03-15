import time  # 引入time模块
import math


def task01(strings):
    A = []
    B = []
    for item in strings:
        num = math.ceil(len(item) / 2)
        A.append(item[:num])
        B.append(item[num:])

    print(''.join(A))
    print(''.join(B))


def task02(strings):
    for elements in strings:
        total = 0
        for i in range(len(elements)):
            flag1 = 0
            flag2 = 0
            for j in range(i, len(elements)):
                if elements[j] == '0':
                    flag1 += 1
                    if flag1 > 1:
                        break
                if elements[j] == '1':
                    flag2 += 1
                    if flag2 > 1:
                        break
                if flag1 == flag2 == 1:
                    total += 1
                    # print(elements[i:j+1])
        print(total)



def task03(strings):
    for elements in strings:
        flag=0
        new=""
        K = 0

        for i in range(len(elements)-1):
            if elements[i]==elements[i+1]:
                flag=1

            else:
                if flag == 0:
                    new += elements[i:i+1]
                else:
                    flag=0
        if elements[-1] != elements[-2]:
            new+=elements[-1]

        print(new)







    '''''''''
    有局限性，对于yxxyxxy来说，无法在第一次消除y之后识别xx后的y也应该消除
    
    for elements in strings:
        sa = []  # 定义一个空列表
        de_str = ''  # 定义一个空字符
        for i in elements:
            if len(sa) == 0:
                sa.append(i)
            else:
                if i == de_str:  # 判断是否与上一个删除元素相同
                    continue  # 相同则不做任何处理
                elif i == sa[-1]:  # 继续判断是否与最后一个元素相
                    de_str = sa.pop(-1)  # 相同赋值给删除字符，不放入列表
                else:
                    sa.append(i)  # 如果都不是，则放入列表
        # print(sa)
        b = "".join(sa)
        print(b)
    '''



'''
3
3
abcxxcbdyyyzzzzfgzzgf
xxyzzyzzyxx
tlmoybbbbptttpavvjssvwhhhhhttenryaaaavlo

ad
None
tlmoyajvwenryvlo

3
1
yzzyzzy
'''


def task04(strings):
    for elements in strings:
        new = []
        for i in range(len(elements)):
            for j in range(i, len(elements)):
                window = elements[i:j + 1]
                if "May" in window:
                    if window.count("May") != 1:
                        break
                    if len(new) == 0:
                        new.append(window)
                    elif len(window) > len(new[-1]):
                        new.clear()
                        new.append(window)
                    elif len(window) == len(new[-1]):
                        new.append(window)
        for item in new:
            print(item)
        print("****")


'''
---------------Input----------------
4
3
MayMayzzAprilzzMayFebruaryJanuaryMayzz
MayMayMayMay
xxMayzzMayttMayuuMaywwMayrr
---------------Output----------------
ayzzAprilzzMayFebruaryJanuaryMa
****
ayMayMa
ayMayMa
****
ayzzMayttMa
ayttMayuuMa
ayuuMaywwMa
****
'''


def task05(strings):
    MonthName = ["January", "February", "March", "April", "June", "July", "August", "September", "October", "November",
                 "December"]
    for elements in strings:
        new = []
        for i in range(len(elements)):
            for j in range(i, len(elements)):
                window = elements[i:j + 1]
                if "May" in window:
                    if window.count("May") != 1 or \
                            any(word if word in window else False for word in MonthName) == True:
                        break
                    if len(new) == 0:
                        new.append(window)
                    elif len(window) > len(new[-1]):
                        new.clear()
                        new.append(window)
                    elif len(window) == len(new[-1]):
                        new.append(window)
        for item in new:
            print(item)
        print("****")


'========================================I N P U T    R E A D I N G========================================'
if __name__ == '__main__':
    taskNo = int(input())
    Nstrings = int(input())
    strings = []
    for k in range(Nstrings):
        strings.append(input())

t1 = time.time()
if taskNo == 1:  task01(strings)
if taskNo == 2:  task02(strings)
if taskNo == 3:  task03(strings)
if taskNo == 4:  task04(strings)
if taskNo == 5:  task05(strings)
t2 = time.time()
# print('time', str(t2 - t1)[:5])
