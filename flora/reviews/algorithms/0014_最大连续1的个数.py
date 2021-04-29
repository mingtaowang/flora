desc = '''
给定一个二进制数组，找出该数组中最大连续1的个数。

-输入数组将只包含0和1。
-输入数组的长度为正整数，不超过10000


例 1:

输入: [1,1,0,1,1,1]
输出: 3
解释: 前两位还有后三位数字是1.
    所以最大连续1的个数为3
    
例 2:

输入: [1]
输出: 1
'''


class Solution:
    """
    @param nums: a binary array
    @return:  the maximum number of consecutive 1s
    """
    def findMaxConsecutiveOnes(self, nums):
        # Write your code here
        i = 0
        res = []
        while i < len(nums):
            if nums[i] != 1:
                i += 1
                continue
            else:
                tmp = 0
                for j in range(i, len(nums)):
                    if nums[j] == 1:
                        tmp += 1
                    else:
                        break

                res.append(tmp)
                i += tmp
        return max(res) if res else 0


if __name__ == '__main__':
    s = Solution()
    origin = [1,1,0,1,1,1]
    res = s.findMaxConsecutiveOnes(origin)
    print(res)
