desc = '''
以字符串的形式给出两个非负整数 num1 和 num2，返回 num1 和 num2 的和。

num1 和 num2 的长度都小于5100。
num1 和 num2 都只包含数字 0-9。
num1 和 num2 都不包含任何前导零。
您不能使用任何内置的BigInteger库内的方法或直接将输入转换为整数。

样例 1:

输入 : num1 = "123", num2 = "45"
输出 : "168"
'''


class Solution:
    """
    @param num1: a non-negative integers
    @param num2: a non-negative integers
    @return: return sum of num1 and num2
    """
    def addStrings(self, num1, num2):
        # write your code here
        res = []
        idx_1 = len(num1) - 1
        idx_2 = len(num2) - 1
        carry = 0
        while idx_1 >= 0 or idx_2 >= 0:
            tmp = carry
            if idx_1 >= 0:
                tmp += int(num1[idx_1])
                idx_1 -= 1
            if idx_2 >= 0:
                tmp += int(num2[idx_2])
                idx_2 -= 1

            carry, left = divmod(tmp, 10)
            res.append(str(left))

        if carry > 0:
            res.append(str(carry))

        return ''.join(reversed(res))


if __name__ == '__main__':
    s = Solution()
    num1 = "123"
    num2 = "45"
    res = s.addStrings(num1, num2)
    print(res)
