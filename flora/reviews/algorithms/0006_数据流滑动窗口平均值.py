desc = '''
给出一串整数流和窗口大小，计算滑动窗口中所有整数的平均值


样例 1：

MovingAverage m = new MovingAverage(3);
m.next(1) = 1 // 返回 1.00000
m.next(10) = (1 + 10) / 2 // 返回 5.50000
m.next(3) = (1 + 10 + 3) / 3 // 返回 4.66667
m.next(5) = (10 + 3 + 5) / 3 // 返回 6.00000
'''


class MovingAverage(object):
    """
    @param: size: An integer
    """
    def __init__(self, size):
        # do intialization if necessary
        self.arr = []
        self.size = size
        self.sum = 0

    """
    @param: val: An integer
    @return:
    """
    def next(self, val):
        # write your code here
        if len(self.arr) < self.size:
            self.arr.append(val)
            self.sum += val
        else:
            if len(self.arr) == self.size:
                self.arr.append(val)
                pop_val = self.arr.pop(0)
                self.sum = self.sum + val - pop_val
        return self.sum / len(self.arr)


if __name__ == '__main__':
    obj = MovingAverage(3)
    print(obj.next(1))
    print(obj.next(10))
    print(obj.next(3))
    print(obj.next(5))
