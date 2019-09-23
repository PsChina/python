#coding=utf-8
import module_a as ma
import module_b as mb

ma.foo()
mb.foo()

print('练习1：实现计算求最大公约数和最小公倍数的函数。')

def gcd(a,b):
  if a<b:
    temp = a
    a = b
    b = temp
  while a%b is not 0:
    temp = a
    a = b
    b = temp%a
  return b

print(gcd(319,377))

def lcm(a,b):
  return a*b/gcd(a,b)

print(lcm(15,24))

print('练习2：实现判断一个数是不是回文数的函数。')

def is_palindrome(num):
  res = True
  if(num<10):
    return True
  else:
    string = str(num)
    length = len(string)
    i = 0
    end = int(length/2) - 1
    if string[i] is not string[length - i - 1]:
      res = False
    i += 1
    while i < end:
      if string[i] is not string[length - i - 1]:
        res = False
      i += 1
  return res

def log(arr):
  for i in range(len(arr)):
    print(is_palindrome(arr[i]))

log([100,101,123,12321,1234321,11])

print('练习3：实现判断一个数是不是素数的函数。')

def is_prime(num):
  if num <=1:
    return False
  for i in range(2,num):
    if num%i is 0:
      return False
  return True

print(is_prime(2))
print(is_prime(3))
print(is_prime(4))
print(is_prime(5))
print(is_prime(6))
print(is_prime(7))

