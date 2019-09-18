# coding=utf-8
x = float(input('x='))
if x > 0:
  print('x 大于零')
elif x==0:
    print('x 等于零')
else:
    print('x 小于零')

# 身份验证
print('身份验证')

username = input('用户名:')

passworld = input('密码:')

if username == 'ps' and passworld == '123456':
  print('验证通过')
else:
  print('验证失败')

# 投骰子决定做什么
print('投骰子决定做什么')

from random import randint

face = randint(1,6)

if face==1:
  result = '唱歌'
elif face==2:
  result = '跳舞'
elif face==3:
  result = '学狗叫'
elif face==4:
  result = '做俯卧撑'
elif face==5:
  result = '说绕口令'
elif face==6:
  result = '讲冷笑话'
print(result)