1.
count=0
def getPentagonalNumber(n):
    global count
    for n in range(1,101):
        wujiaoshu = n * (3*n-1)//2
        count += 1
        print(wujiaoshu,end = '\t')
        if count % 10 == 0:
            print('\n',end = '')
getPentagonalNumber(1)

2.
word = input('请输入整数：')
i = len(word)
list_num = []
def sumDigits(word):
    global i
    global list_num
    for n in range(len(word)):
        a=int(word)%10
        word=str(int(word)//10)
        list_num.append(a)
        i -= 1
        if i == 0:
            sum_ = sum(list_num)
            print(sum_)
sumDigits(word)

3.
num1 = input('请输入一个数字1：')
num2 = input('请输入一个数字2：')
num3 = input('请输入一个数字3：')
def displaySortedNumbers(num1,num2,num3):
    list = [num1,num2,num3]
    a = sorted(list)
    return a
print('排序后为：',displaySortedNumbers(num1,num2,num3))


5.
count=0
ch1 = 73
ch2 = 91
def printChars(ch1,ch2):
    global count
    for i in range(ch1,ch2):
        count += 1
        print(chr(i),end = " ")
        if count % 10 == 0:
            print("\n")
print(printChars(ch1,ch2))


6.
count=1
year1=2010
year2=2021
def numberOfDaysInAYear(year1,year2):
    for i in range(year1,year2):
        if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
            print(i,'年有366天，是闰年')
        else:
            print(i,'年有365天，是平年')
print(numberOfDaysInAYear(year1,year2))


7.
def distance(x1,x2,y1,y2):
    d=((x1-x2)**2+(y1-y2)**2)**0.5
    print("两点间距离为：",'%.2f'%d)
distance(2,3,4,5)



9.
import time
def main():
    localtime = time.localtime(time.time())
    print("本地时间为：",localtime)
    ticks = time.time()*1000
    print("距离当前时间毫秒为：",ticks)
main()

10.
import random
def main():
    a=random.choice([1,2,3,4,5,6])
    b=random.choice([1,2,3,4,5,6])
    if a+b==2 or a+b==3 or a+b==12:
        print('%d + %d = %d'%(a,b,a+b))
        print('你输了')
    elif a+b==7 or a+b==11:
        print('%d + %d = %d'%(a,b,a+b))
        print('你赢了')
    else:
        print('%d + %d = %d'%(a,b,a+b))
        c=random.choice([1,2,3,4,5,6])
        d=random.choice('1','2','3','4','5','6')
        if c+d == 7:
            print('%d + %d = %d'%(c,d,c+d))
            print('你输了')
        elif c+d == a+b:
            print('%d + %d = %d'%(c,d,c+d))
            print('你赢了')
main()

