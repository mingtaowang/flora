'''
求1000以内的完全数（如果一个数恰好等于它的因子之和，则称该数为“完全数”，又称完美数或完备数。
例如：第一个完全数是6，它有约数1、2、3、6，除去它本身6外，其余3个数相加，1+2+3=6。
第二个完全数是28，它有约数1、2、4、7、14、28，除去它本身28外，其余5个数相加，1+2+4+7+14=28。）
'''


class Solution:

    def mems(self, n):
        res = []
        for item in range(1, n):
            sum = 0
            for i in range(1, item):
                if item % i == 0:
                    sum += i

            if sum == item:
                res.append(item)

        return res


if __name__ == '__main__':
    s = Solution()
    n = 1000
    res = s.mems(n)
    print(res)
