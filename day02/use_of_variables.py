# coding=utf-8
# 除
print(4.2 / 3)
print(3 / 1.7)
# 整除
print(4.2 // 3)
print(3 // 1.7)
# 取模(取余数)
print(4.2 % 2)
print(3 % 1.5)
# 指数运算
print(2 ** 8)

# value_a = float(input('a = '))

# value_b = float(input('b = '))

# print('%f + %f= %f' % (value_a, value_b, value_a + value_b))

# print('%f %% %f = %f' % (value_a, value_b, value_a % value_b))

# print('%f * %f = %f' % (value_a, value_b, value_a * value_b))

# int 对应 %d

# value_a = complex(input('a = '))

# value_b = complex(input('b = '))

# print('%s + %s= %s' % (value_a, value_b, value_a + value_b))

# print('%s %% %s = %s' % (value_a, value_b, value_a % value_b))

# print('%s * %s = %s' % (value_a, value_b, value_a * value_b))

# 复数加减法 实部+实部等于实部， 虚部+虚部等于虚部。
# 复数乘法 a+bj * c+dj = (ac-bd)+(bc+ad)j。

print(1 is True)
print( (1 == 1) is True)
print( type('2'), type(2) )
print( type('2') is not type(2) )
print( 2 and 0 is 0 )
print( 0 or 3 is 3 )
print( True is not False )

print('练习1：华氏温度转摄氏温度。')

t = float(input('请输入华氏度:'))

c = (t - 32)/1.8

print('%.2f华氏度等于%.2f摄氏度' % (t, c))

import math

print('练习2：输入圆的半径计算计算周长和面积。')

r = float(input('半径:'))

perimeter = 2 * r * math.pi

area = math.pi * (r ** 2)

print('半径%f的圆周长为%.4f,面积为%.4f'%(r,perimeter,area))

print('练习3：输入年份判断是不是闰年。')

year = int(input('请输入年份:'))

is_leap = year % 4 is 0 or year % 400 is 0

print(is_leap)