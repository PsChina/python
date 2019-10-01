#coding=utf-8

# day 10

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


# day 11 

# 静态方法和类方法

from math import sqrt

class Triangle(object):
  def __init__(self,a,b,c):
    self._a = a
    self._b = b
    self._c = c
  @staticmethod
  def is_valid(a,b,c):
    return a + b > c and a + c > b and b + c > a

  def perimeter(self):
      return self._a + self._b + self._c

  def area(self):
        half = self.perimeter() / 2.0
        return sqrt(half * (half - self._a) *
                    (half - self._b) * (half - self._c))
  @classmethod
  def getAreaFromTriangle(cls,a,b,c):
    if cls.is_valid(a,b,c):
      triangle = Triangle(a,b,c)
      return triangle.area()
    else:
      print('无法构成三角形')



a,b,c = 2,2,3

if Triangle.is_valid(a,b,c):
  triangle = Triangle(a,b,c)
  print(triangle.perimeter())
  print(triangle.area())
else:
  print('无法构成三角形')

print(Triangle.getAreaFromTriangle(1,1,1))

# day12 

# 继承

class Person(object):
  def __init__(self,name,age):
    self._name = name
    self._age = age
  @property
  def name(self):
    return self._name
  @name.setter
  def name(self,new_name):
    self._name = new_name
  @property
  def age(self):
    return self._age
  @age.setter
  def age(self, new_age):
    self._age = new_age

class Student(Person):
  def __init__(self,name,age):
      super().__init__(name,age)
  def learn(self):
      print('Learing')

class Teacher(Person):
  def __init__(self,name,age):
      super().__init__(name,age)
  def teach(self):
      print('Teaching')

student = Student('潘杉杉',18)

teacher = Teacher('Github',28)

teacher.teach()
print(teacher.name,teacher.age)
student.learn()
print(student.name,student.age)

# day13

# 多态

from abc import ABCMeta, abstractmethod

class Pet(object, metaclass=ABCMeta):
  def __init__(self,nickname):
    self._nickname = nickname
  @abstractmethod
  def make_voice(self):
    """发出声音"""
    pass

class Dog(Pet):
  def make_voice(self):
    print("%s汪汪汪" % self._nickname)

class Cat(Pet):
  def make_voice(self):
    print("%s喵喵喵" % self._nickname)

def main():
  pets = [Dog('旺财'),Cat('凯蒂')]
  for pet in pets:
    pet.make_voice()

if __name__ == '__main__':
  main()
