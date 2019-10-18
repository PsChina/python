#coding=utf-8
def fib(num, temp = {}):
  if num in range(0, 2):
    return 1
  try:
    return temp[num]
  except KeyError:
    temp[num] = fib(num - 1) + fib(num - 2)
    return temp[num]
  
if __name__ == '__main__':
  num = int(input('请输入要求的斐波拉契数列项数:')) - 1
  print(fib(num))