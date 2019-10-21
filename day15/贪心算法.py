#coding=utf-8
# 物品名称 重量 价值
arr = [('A',1,2),('B',2,1),('C',10,4),('D',3,6),('E',20,22),('F',3,9)]
class Item(object):
    def __init__(self,name,weight,price):
        self.name = name
        self.weight = weight
        self.price = price
        self.value = price/float(weight)


def main():
    max_weight = 10
    lenght = len(arr)
    for index in range(lenght):
        item = arr[index]
        arr[index] = Item(item[0],item[1],item[2])
    arr.sort(key=lambda x:x.value, reverse=True)
    total_weight = 0
    total_value = 0
    for item in arr:
        if total_weight + item.weight <= max_weight:
            print('小偷拿走了 %s' % item.name)
            total_weight += item.weight
            total_value += item.price
    print(total_weight,total_value)
        


if __name__ == '__main__':
    main()
