#coding=utf-8
from time import time
from threading import Thread

import requests

# class DownloadHandler(Thread):

#   def __init__(self, url):
#     super().__init__()
#     self.url=url
  
#     def run(self):
#         filename = self.url[self.url.rfind('/') + 1:]
#         resp = requests.get(self.url)
#         with open('/Users/Hao/' + filename, 'wb') as f:
#             f.write(resp.content)


def main():
  # 通过requests模块的get函数获取网络资源
  # 下面的代码中使用了天行数据接口提供的网络API
  # 要使用该数据接口需要在天行数据的网站上注册
  # 然后用自己的Key替换掉下面代码的中APIKey即可
  resp = requests.get(
      'http://api.tianapi.com/meinv/?key=APIKey&num=10')
  # 将服务器返回的JSON格式的数据解析为字典
  data_model = resp.json()
  print(data_model)
  for mm_dict in data_model:
      print(data_model[mm_dict])


if __name__ == '__main__':
  main()