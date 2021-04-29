desc = '''
一个镜像数字是指一个数字旋转180度以后和原来一样(倒着看)。例如，数字"69"，"88"，和"818"都是镜像数字。
写下一个函数来判断是否这个数字是镜像的。数字用字符串来表示


样例1:

输入 : "69" 
输出 : true

样例 2:

输入 : "68" 
输出 : false
'''


class Solution:
    """
    @param num: a string
    @return: true if a number is strobogrammatic or false
    """
    def isStrobogrammatic(self, num):
        # write your code here
        if num == '' or num is None:
            return False

        if len(num) == 1:
            return True if num in ['8', '1', '0'] else False

        patterns = {'6': '9', '9': '6', '8': '8', '1': '1', '0': '0'}
        length = len(num)
        mid = length // 2 - 1 if length % 2 == 0 else length // 2
        res = True
        for i in range(mid + 1):
            item = num[i]
            if item not in patterns:
                res = False
                return res

            right = patterns.get(item)
            if num[length - i - 1] == right:
                continue
            else:
                res = False
                return res
        return res


if __name__ == '__main__':
    s = Solution()
    origin = '08'
    res = s.isStrobogrammatic(origin)
    print(res)
