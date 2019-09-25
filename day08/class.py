#coding=utf-8
class Hello():
  def __init__(self):
    print('Hello world')


sayhello = Hello()

class Student():
  def __init__(self,name,age):
    self.name = name
    self.age = age

p = Student('潘杉杉',27)

print(p.name,p.age)

class Test:
  def __init__(self,foo):
    self.__foo = foo
  def __bar(self):
    print(self.__foo)
    print('__bar')

test = Test('Hello')

# test.__bar()

# print(test.__foo)



