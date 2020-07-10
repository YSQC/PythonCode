class MyArray:
    """自定义list"""
    def __init__(self, capacity):
        self._data = []
        self._capacity = capacity # 最大容量

    def __getitem__(self, position):
        print('调用了__getitem__方法')
        return self._data[position]

    def __setitem__(self, index, value):
        self._data[index] = value

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        for item in self._data:
            print('调用了__iter__方法')
            yield item

    def find(self, index):
        try:
            return self._data[index]
        except IndexError:
            print('该位置为空!!!')

    def index(self, value):
        try:
            return self._data.index(value)
        except ValueError:
            print('该值不在列表中') # 默认返回None

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
