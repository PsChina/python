#coding=utf-8
def bubble_sort(array):
  length = len(array) - 1
  for i in range(length):
    for j in range(length - i):
      if array[j]>array[j+1]:
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp


if __name__ == '__main__':
  arr = [5,1,9,2,11,-1,-10,0,4]
  bubble_sort(arr)
  print(arr)

    
