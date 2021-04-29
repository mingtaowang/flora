desc = '''
有一个数组nums，以及三个正整数k,u,l。
对于nums的所有长为k的子段，如果它的总和小于u，就得1分，如果它的总和大于l，就扣1分。
请求出最终能获得多少分？

nums为列表
nums的长度为n，1 <= n <= 10的5次方
k, 字列表的长度
u，字列表中的所有元素的总和小于u，得1分
l，字列表中的所有元素的总和大于l，扣1分

样例输入:
nums = [0, 1, 2, 3, 4]
k = 2
u = 2
l = 5
样例输出:
0
'''


class Solution:
    """
    @param nums: the array to be scored.
    @param k: the requirement of subarray length.
    @param u: if the sum is less than u, get 1 score.
    @param l: if the sum is greater than l, lose 1 score.
    @return: return the sum of scores for every subarray whose length is k.
    """
    def arrayScore(self, nums, k, u, l):
        # write your code here.

        score = 0
        sumOfSubarray = 0

        for i in range(k):
            sumOfSubarray += nums[i]

        if sumOfSubarray < u:
            score += 1

        if sumOfSubarray > l:
            score -= 1

        for index in range(1, len(nums) - k + 1):
            sumOfSubarray = sumOfSubarray - nums[index - 1] + nums[index + k - 1]

            if sumOfSubarray < u:
                score += 1

            if sumOfSubarray > l:
                score -= 1
        return score


if __name__ == '__main__':
    s = Solution()
    nums = [0, 1, 2, 3, 4]
    k = 2
    u = 2
    l = 5
    res = s.arrayScore(nums, k, u, l)
    print(res)
