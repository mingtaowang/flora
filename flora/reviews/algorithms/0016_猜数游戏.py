desc = '''
我们正在玩猜数游戏。 游戏如下：
我从 1 到 n 选择一个数字。 你需要猜我选择了哪个号码。
每次你猜错了，我会告诉你这个数字与你猜测的数字相比是大还是小。
你调用一个预定义的接口 guess(int num)，它会返回 3 个可能的结果(-1，1或0):
-1代表这个数字小于你猜测的数
1代表这个数字大于你猜测的数
0代表这个数字等于你猜测的数


样例 1:

输入 : n = 10, 我选择了 4 (但是你不知道)
输出 : 4
'''


class Solution:
    # @param {int} n an integer
    # @return {int} the number you guess
    def guessNumber(self, n):
        # Write your code here
        l = 1
        r = n
        while l <= r:
            mid = l + (r - l) / 2
            res = Guess.guess(mid)
            if res == 0:
                return mid
            if res == -1:
                r = mid - 1
            if res == 1:
                l = mid + 1
        return -1


if __name__ == '__main__':
    s = Solution()
    origin = 10
    res = s.guessNumber(origin)
    print(res)
