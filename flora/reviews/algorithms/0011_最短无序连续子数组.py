desc = '''
给定一个整数数组，你需要找到一个连续子数组，如果你只按升序对这个子数组进行排序，那么整个数组也将按升序排序。

你需要找到最短的这样的子数组并输出它的长度。

输入的数组长度范围为[1, 10,000]。
输入的数组可能会包含重复元素，本题升序的含义为<=。


输入: [2, 6, 4, 8, 10, 9, 15]
输出: 5
解释: 你需要对[6, 4, 8, 10, 9]按升序排列从而整个数组也变为升序。
'''


class Solution:
    """
    @param nums: an array
    @return: the shortest subarray's length
    """
    def findUnsortedSubarray(self, nums):
        # Write your code here
        sorted_nums = sorted(nums)
        length = len(nums)
        while length > 0 and nums[length - 1] == sorted_nums[length - 1]:
            length -= 1

        temp = 0
        for i in range(length):
            if nums[i] == sorted_nums[i]:
                temp += 1
            else:
                break
        return length - temp


if __name__ == '__main__':
    s = Solution()
    origin = [2, 6, 4, 8, 10, 9, 15]
    res = s.findUnsortedSubarray(origin)
    print(res)
