desc = '''
给定一个整数，写一个函数来确定它是否是2的幂


样例 1:

输入: n = 3
输出: false
'''


class Solution:
    """
    @param n: an integer
    @return: if n is a power of two
    """
    def isPowerOfTwo(self, n):
        # Write your code here
        if n <= 0:
            return False

        return n & n - 1 == 0


if __name__ == '__main__':
    s = Solution()
    origin = 4
    res = s.isPowerOfTwo(origin)
    print(res)
