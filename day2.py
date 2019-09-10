7.18-1.
import math
a = float(input('请输入a的值：'))
b = float(input('请输入b的值：'))
c = float(input('请输入c的值：'))
root = b*b - 4*a*c
if root > 0:
    x1 = (-b + math.sqrt(root))/(2*a)
    x2 = (-b - math.sqrt(root))/(2*a)
    print(x1 , x2)
elif root == 0:
    x = -b / 2*a
    print(x)
else:
    print('The equation has no real rools')



7.18-2.
import random
num1 = random.randint(0,100)
print(num1)
num2 = random.randint(0,100)
print(num2)
sum = input('请输入两数之和:')
if sum == num1 + num2:
    print('True')
else:
    print('False')

7.18-3.
def week(day):    
	if day == 0:
	    print('星期日')
	elif day == 1:
	    print('星期一')
	elif day == 2:
	    print('星期二')
	elif day == 3:
	    print('星期三')
	elif day == 4:
	    print('星期四')
	elif day == 5:
	    print('星期五')
	elif day == 6:
	    print('星期六')	        
def today(day,day_1):
	day_2 = day+day_1
	if day_2>=7:
	    day_3 = (day_2)%7
	    week(day_3)
	else:
	    week(day_2)
def sart():
	day = eval(input('请输入今天是哪一天：'))
	day_1 = eval(input('输入到哪天的天数'))
	week(day)
	today(day,day_1)
sart()


7.18-4.
def count(a,b,c):
	num = [a,b,c]
	num.sort()
	print(num)
def start():
	a = int(input('输入第一个整数：'))
	b = int(input('输入第二个整数：'))
	c = int(input('输入第三个整数：'))
	count(a,b,c)
start()


7.18-5.
def shop(weight1,weight2,price1,price2):
	package1 = weight1 / price1
	package2 = weight2 / price2
	if package1 > package2:
	    print('package1 has the better price')
	else:
	    print('package2 has the better price')
def start():
	weight1 = float(input('第一种重量是:')) 
	price1 = float(input('第一种价格是:'))
	weight2 = float(input('第二种重量是:'))
	price2 = float(input('第二种价格是:'))
	shop(weight1,weight2,price1,price2)
start() 


7.18-6.
import calendar 
def num(year,month):
	print(calendar.monthrange(year, month)[1])
def start():
	year = int(input('Enter year: ')) 
	month = int(input('Enter month number: '))
	num(year,month)
start()


7.18-7
import random
def chaoxiang(sum):
	0 == '正面'
	1== '反面'
	a = random.randint(0,1)
	if a == sum:
	    print("正确")
	else:
	    print("错误")
def Start():
	sum = input("硬币显示的是： ")
	chaoxiang(sum)
Start()


7.18-8
import random
def caiquan(people):
	0 == '剪刀'
	1 == '石头'
	2 == '布'
	c = random.randint(0,2)
	print(c)
	if people == c:
	    print('平局')
	else:
	    if c == 0 and people == 1:
	        print('电脑赢了')
	    elif c == 1 and people == 2:
	        print('电脑赢了')
	       
	    elif c == 2 and people == 0:
	        print('电脑赢了')
	       else:
	        print('你赢了')
def start():
	people = int(input('请你出拳：'))
	caiquan(people)
start()


7.18-9
def main(year,m,d):
    a = ['周六','周日','周一','周二','周三','周四','周五']
    if m == 1:
        m = 13
        year = year - 1
    if m ==2:
        m = 14
        year = year - 1
    h = int(d+((26*(m+1))//10)+(year%100)+((year%100)/4)+((year//100)/4)+5*year//100)%7
    day = a[h]
    print('那一天是一周中的:%s' %day)
def Start():
    year = int(input('输入哪一年:'))
    m = int(input('输入月份1-12:'))
    d = int(input('输入月份第几天1-31:'))
    main(year,m,d)
Start()


7.18-10
import random
def pai():
	shu = ["a",2,3,4,5,6,7,8,9,10,"jack","queen","king"] 
	hua = ["梅花","红桃","方块","黑桃"]
	a = random.choice(shu)
	b = random.choice(hua)
	print("这张是{}{}".format(b,a))
pai()


7.18-11
def num():
	a = int(input('请输入一个正整数: '))
	b = a
	c = 0
	while b > 0:
	    c *= 10
	    c += b % 10
	    b //= 10
	if a == c:
	    print('%d是回文数' % a)
	else:
	    print('%d不是回文数' % a)
def start():
	num()
start()


7.18-12
def bian(b1,b2,b3):
	a = b1 + b2
	b = b1 + b3
	c = b2 + b3
	if a>b3 or b>b2 or c>b1:
		print('合法')
		C = b1+b2+b3
		print("周长是：",C)
	else:
		print('不合法')
def start():
	b1 = int(input('第一条边长：'))
	b2 = int(input('第二条边长：'))
	b3 = int(input('第三条边长：'))
	bian(b1,b2,b3)
start()

7.19-1
a = 0
b = 0
sum = 0
count = 1
while count != 0:
	count = int(input('请输入数字：'))
	if count > 0:
	    a += 1  
	elif count < 0:
	     b += 1  
	sum += count
print('负数个数为：%d'%b)
print('正数个数为: %d'%a)
averg = sum / (a + b)
print('平均值为： %f'%averg)

7.19-2
a = [10000]
for i in range(14):
	x = a[i] * 1.05
	a.append(x)
print('十年后的学费是：%.2f'%a[14])
print('现在及十年后的学费是：%.2f'%sum(a))


7.19-3
t = 0
for i in range(100,1000):
	if i % 5 == 0 and i % 6 == 0:
	    print(i,end = ' ')
	    t += 1
	if t % 10 == 0:
	    print( )


7.19-4
num = 0
i = 200
while i**2 > 12000:
	i -= 1
print(i)
while num**2 <12000:
	num += 1
print(num)


7.19-5
a = 0
n = 0 
while n >= 0:
	n +=1
	a += 1/n
	if n == 50000:
	    print(a)
	    break
n = 50001 
while n <= 50001:
	n -=1
	a += 1/n
	if n == 1:
	    print(a)
	    break


7.19-6
a = 1
b = 3
c = 0
while a >=1:
	c += a/b
	a += 2
	b += 2
	if a > 97:
	    print(c)
	    break


7.19-7
i = 1
pi = 0
while i > 0:
	a = 4*((-1)**(i+1)/(2*i-1))
	i += 1
	pi += a
	if i % 10000 == 0:
	    print(pi)
	elif i > 10000:
	    break


7.19-8
for i in range(1,10000):
	num = 0
	for j in range(1,i):
	    if i % j ==0:
	        num += j
	if i == num:
	    print(i)


7.19-9
a = 0
for i in range(1,8,2):
	for j in range(2,8):
	    if i != j:
	        print(i,j)
	        a += 1
print(i)
