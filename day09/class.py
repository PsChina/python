#coding=utf-8

class Student():
  def __init__(self,name):
    self.__name = name
  @property
  def name(self):
    return self.__name
  @name.setter
  def name(self, new_name):
    self.__name = new_name

student = Student('潘杉杉')

print(student.name)

student.name = '潘杉'

print(student.name)
