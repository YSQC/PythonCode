class MyArray:
    """自定义一个数组类"""
    def __init__(self, capacity):
        self._data = []
        self._capacity = capacity # 最大容量

    def __getitem__(self, position):
        return self._data[position]

    def __setitem__(self, index, value):
        self._data[index] = value

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        """for循环时被调用,此时MyArray对象为可迭代对象"""
        for item in self._data:
            yield item

    def find(self, index):
        try:
            return self._data[index]
        except IndexError:
            print('不存在!!!')

    def delete(self, index):
        try:
            self._data.pop(index)
            return True
        except IndexError:
            return False

    def insert(self, index, value):
        if len(self) >= self._capacity: # 超出最大容量时,不能继续插入元素
            return False
        else:
            return self._data.insert(index, value)

    def clear(self):
        self._data = []

    def print_all(self):
        print(self._data)


def operate():
    array = MyArray(5)
    array.insert(0, 0)
    array.insert(1, 1)
    array.insert(2, 2)
    array.insert(3, 3)
    array.delete(3)
    array.find(8)
    print('0号位置元素为:', array[0]) # __getitem__方法被调用
    array[0] = 1000000 # __setitem__方法被调用
    print('array长度为', len(array)) # __len__方法被调用
    for i in array: # __iter__方法被调用,若无__iter__方法,则调用__getitem__方法
        print(i)
    array.print_all()
    array.clear()
    array.print_all()


if __name__ == "__main__":
    operate()

