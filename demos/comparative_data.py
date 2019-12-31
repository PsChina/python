
#coding=utf-8

def comparative_data(objectA,objectB,keys=[]):
  typeA = type(objectA)
  typeB = type(objectB)
  # 默认两个对象是一致的
  isNoDifference = True
  # 如果类型不一致则两个对象不一致
  if typeA.__name__ != typeB.__name__:
    return False
  # 如果这个对象是个字典
  elif typeA.__name__ == 'dict':
    length = len(keys)
    # 如果没有指定要比较的属性 拿到属性最多的对象的所有属性进行比较 如果有则按照指定属性比较数据是否一致
    if length == 0:
      keysA = objectA.keys()
      keysB = objectB.keys()
      lengthA = len(keysA)
      lengthB = len(keysB)
      if lengthA > lengthB:
        keys = keysA
        length = lengthA
      else:
        keys = keysB
        length = lengthB
    # 开始比较
    for index in range(0,length):
      key = keys[index]
      # 如果两个对象都存在这个属性
      if key in objectA and key in objectB:
        # 调用比较两个数据是否相等的函数（comparative_data）进行比较得到他们是否相等的结论
        _isNoDifference = comparative_data(objectA[key],objectB[key])
        # 因为一开始默认两个数据是一样的所以只更新不相等的情况
        if _isNoDifference is False:
          isNoDifference = _isNoDifference
      # 如果两个对象有一个不存在这个属性 那么他们不想等
      elif key in objectA and objectB.has_key(key) is False or objectA.has_key(key) is False and key in objectB:
        isNoDifference = False
  # 如果这个对象是个数组
  elif typeA.__name__ == 'list':
    lengthA = len(objectA)
    lengthB = len(objectB)
    # 如果长度不一返回 False
    if lengthA != lengthB:
      return False
    length = lengthA
    # 长度相等调用比较两个数据是否相等的函数（comparative_data）挨个比较数组内的数据是否一致
    for index in range(0, length):
      # 因为一开始默认两个数据是一样的所以只更新不相等的情况
      if comparative_data(objectA[index],objectB[index],keys) is False:
        isNoDifference = False
  # 如果这个对象既不是数组也不是字典 直接比较 是否相等
  else:
    return objectA == objectB
  return isNoDifference


# 测试

classA = {
  'name':'classA',
  'teachers':['A'],
  'students':['A','B'],
  'detail':{
    'A':'A',
    'B':'B',
    'C':[1,2]
  }
}

classB = {
  'name':'classA',
  'teachers':['A'],
  'students':['C','D'],
  'detail':{
    'A':'A',
    'B':'B',
    'C':[1]
  }                 
}

# 指定比较 detail 结果 False
print(comparative_data(classA,classB,['detail']))
# 指定比较 name, teachers 结果 True
print(comparative_data(classA,classB,['name','teachers']))
# 比较整个对象 结果 False
print(comparative_data(classA,classB))
# 比较数组 结果True
print(comparative_data([1,2,3,{'a':'a'}],[1,2,3,{'a':'a'}]))
# 比较数组 结果False
print(comparative_data([1,2,3,{'a':'a'}],[1,2,3,{'a':'a','b':'b'}]))
# 比较数组 结果False
print(comparative_data([1,2,3,{'a':'a','b':'b'}],[1,2,3,{'a':'a'}]))
# 比较数组 结果True
print(comparative_data([1,2,3,{'a':'a','b':'b'}],[1,2,3,{'a':'a','b':'b'}]))
# 比较数组 指定比较 a 属性 True
print(comparative_data([1,2,3,{'a':'a','b':'b'}],[1,2,3,{'a':'a'}],['a']))
# 比较数组 结果False
print(comparative_data([1,2,3],[1]))
# 比较数字 结果 True
print(comparative_data(1,1))
# 比较数字 结果 False
print(comparative_data(1,2))
# 比较字符串 结果 False
print(comparative_data('1','2'))