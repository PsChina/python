#coding=utf-8
from math import sqrt
print('练习1：输入一个数判断是不是素数。')

num = int(input('请输入一个正整数num='))

end = int(sqrt(num))

is_prime_num = True

for x in range(2,end+1):
  if num % x is 0:
    is_prime_num = False
    break
if is_prime_num and num is not 1:
  print('%d 是素数' % num)
else:
  print('%d 不是素数' % num)

print('练习2：输入两个正整数，计算最大公约数和最小公倍数。')

num_a = int(input('A='))

num_b = int(input('B='))

a = num_a
b = num_b
# 辗转相除法

if num_a < num_b:
  temp = num_a
  num_a = num_b
  num_b = temp

mod = num_a % num_b

while mod is not 0:
  num_a = num_b
  num_b = mod
  mod = num_a % num_b

print("%d 和 %d 的最大公约数为 %d " % (a, b, num_b))

print("%d 和 %d 的最小公倍数为 %d " % (a, b, a*b/num_b))


print('练习3：打印三角形图案。')

"""
打印各种三角形图案

*
**
***
****
*****

    *
   **
  ***
 ****
*****

    *
   ***
  *****
 *******
*********

"""

for i in range(5):
  for _ in range(i+1):
    print('*', end='') # python3
  print()

for i in range(5):
  for _ in range(5-i-1):
    print(' ', end='') # python3
  for _ in range(i+1):
    print('*', end='')
  print()

for i in range(5):
  for _ in range(5-i-1):
    print(' ', end='') # python3
  for _ in range(2*i+1):
    print('*', end='')
  print()