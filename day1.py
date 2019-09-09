1.
c=float(input('请输入摄氏度：'))
f=1.8*c+32
print('%.2f' %f)
2.
import math
radius=float(input('请输入半径：'))
length=float(input('请输入高：'))
area = radius * radius * math.pi
volume = area * length
print('面积是 %.2f' %area)
print('体积是 %.2f' %volume)
3.
f=float(input('请输入英尺数：'))
m=f * 0.305
print('米数为 %.2f' %m)
4.
f=float(input('请输入最终温度：'))
i=float(input('请输入初始温度：'))
m=float(input('请输入水量：'))
Q = m * (f - i) * 4184
print('能量为 %.2f' %Q)
5.
c=float(input('请输入差额为：'))
n=float(input('请输入年利率为：'))
l=c * (n/1200)
print('利息为 %.5f' %l)
6.
v0=float(input('请输入初始速度为：'))
v1=float(input('请输入末速度为：'))
t=float(input('请输入时间为：'))
a=(v1-v0)/t
print('加速度为 %.5f' %a)
7.
num = float(input('请输入每月存款数：'))
rate = 0.05 / 12
interest = 1 + rate
count =[0]
for i in range(6):
    month = (100 + count[i]) * interest
    count.append(month)
print('六个月后的账户总额：%.2f' % count[6])
8.
num = int(input('请输入一个整数：'))
bai = int(num % 10)
shi = int(num /10 % 10)
ge = int(num /100)
sum = shi + bai + ge
print('各位数字之和：',sum)



import math
radius = float(input('请输入圆的半径: '))
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius
print('周长: %.2f' % perimeter)
print('面积: %.2f' % area)

year = int(input('请输入年份: '))
is_leap = (year % 4 == 0 and year % 100 != 0 or year % 400 == 0)
print(is_leap)

a = 5
b = 10
c = 3
d = 4
e = 5
a += b
a -= c
a *= d
a /= e
print("a = ", a)

flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not flag1
print("flag1 = ", flag1)
print("flag2 = ", flag2)
print("flag3 = ", flag3)
print("flag4 = ", flag4)
print("flag5 = ", flag5)
print(flag1 is True)
print(flag2 is not False)

f = float(input('请输入华氏温度: '))
c = (f - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (f, c))

import hashlib
str = '666@qq.com'
m = hashlib.md5()
b = str.encode(encoding='utf-8')
m.update(b)
str_md5 = m.hexdigest()
print('MD5加密前为 ：' + str)
print('MD5加密后为 ：' + str_md5)

