#coding=utf-8
from multiprocessing import Process
from random import randint
from time import time,sleep

def download(filename):
  time_to_download = randint(2,5)
  sleep(time_to_download)
  print('%s 下载完成耗时 %d 秒' % (filename, time_to_download))

def main():
  start = time()
  # download('1.jpg')
  # download('2.jpg')
  p1 = Process(target=download,args=('1.jpg',))
  p2 = Process(target=download,args=('2.jpg',))
  p1.start()
  p2.start()
  p1.join()
  p2.join()
  end = time()
  print('总共耗时 %.2f 秒.' % (end-start) )

if __name__ == '__main__':
  main()
  print('end')