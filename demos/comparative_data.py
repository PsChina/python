
#coding=utf-8

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

def comparative_data(objectA,objectB,keys=[]):
  typeA = type(objectA)
  typeB = type(objectB)
  isNoDifference = True
  if typeA.__name__ != typeB.__name__:
    return False
  elif typeA.__name__ == 'dict':
    length = len(keys)
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
    for index in range(0,length):
      key = keys[index]
      if key in objectA and key in objectB:
        typeA = type(objectA[key])
        typeB = type(objectB[key])
        if typeA.__name__ == typeB.__name__:
          if typeA == 'list' or typeA == 'dict':
            _isNoDifference = comparative_data(objectA[key],objectB[key],keys)
            if _isNoDifference is False:
              isNoDifference = _isNoDifference
          elif objectA[key] != objectB[key]:
            isNoDifference = False
      elif key in objectA and objectB.has_key(key) is False or objectA.has_key(key) is False and key in objectB:
        isNoDifference = False
  elif typeA.__name__ == 'list':
    lengthA = len(objectA)
    lengthB = len(objectB)
    if lengthA != lengthB:
      return False
    length = lengthA
    for index in range(0, length):
      if comparative_data(objectA[index],objectB[index],keys) is False:
        isNoDifference = False
  return isNoDifference

print(comparative_data(classA,classB,['name','teachers','detail']))

print(comparative_data(classA,classB,['name','teachers']))

print(comparative_data(classA,classB,['name','students']))

print(comparative_data(classA,classB))

print(comparative_data([1,2,3,{'a':'a'}],[1,2,3,{'a':'a'}]))

print(comparative_data([1,2,3,{'a':'a'}],[1,2,3,{'a':'a','b':'b'}]))

print(comparative_data([1,2,3,{'a':'a','b':'b'}],[1,2,3,{'a':'a'}]))

print(comparative_data([1,2,3,{'a':'a','b':'b'}],[1,2,3,{'a':'a','b':'b'}]))

print(comparative_data([1,2,3,{'a':'a','b':'b'}],[1,2,3,{'a':'a'}],['a']))

print(comparative_data([1,2,3],[1]))