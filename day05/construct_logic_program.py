#coding=utf-8
print('寻找水仙花数')

for n in range(100,1000):
  a=n%10
  b=n%100/10
  c=n/100
  if (a**3 + b**3 + c**3) == n:
    print(n)

# print('寻找完美数2-9999')

# for n in range(2,10000):
#   sum = 1
#   is_prime_num = True
#   for x in range(2,n):
#     if n%x is 0:
#       sum += x
#   if sum == n:
#     print(n)

print('百钱百鸡')

for a in range(1,100):
  for b in range(1,100):
    price = a*5+b*3+(100-a-b)*0.33333333
    if price>99.99 and price<100.01:
      print(a,b,100-a-b)


print('斐波那契数列')

a = 1
b = 1
r = 1

for i in range(100):
  if i == 0 or i == 1: 
    r = 1
  else:
    a = b
    b = r
    r = a + b
  print(r)
