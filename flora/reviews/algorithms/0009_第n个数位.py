desc = '''
找出无限正整数数列1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...中的第n个数位。
n是一个正整数，并且不会超出32位有符号整数的范围（n < 2^31）

题目的意思是有一个以正整数（1,2,3,4，依次向后加1）为基础组成的序列（也可以理解为字符串），传入一个整数n，找出在该序列中的第n位数字。该序列含有以下规律：

1-9，有9个一位数，当n小于等于9的时候，可以在里面找到值。
10-99，有90个两位数，当n大于9且小于等于180+9=189时，可以在里面找到值。
100-999，有900个三位数，当n大于189且小于900x3+189=2889时，可以在里面找到值。


样例 1:

输入：3
输出：3

样例 2:

输入：11
输出：0
解析：数字序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... 第11位是0
'''


class Solution:
    """
    @param n: a positive integer
    @return: the nth digit of the infinite integer sequence
    """
    def findNthDigit(self, n):
        # write your code here
        if n <= 9:
            return n

        len = 1     # 数的长度
        count = 9   # 当前长度的数有多少个
        start = 1   # 开始的数

        while n > len * count:
            n -= len * count
            len += 1
            count *= 10
            start *= 10

        start += (n - 1) // len
        index = (n - 1) % len
        return int(str(start)[index])


if __name__ == '__main__':
    s = Solution()
    origin = 11
    res = s.findNthDigit(origin)
    print(res)
