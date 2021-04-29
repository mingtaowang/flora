desc = '''
“回文串”是一个正读和反读都一样的字符串，比如“level”或者“noon”等等就是回文串。

给出一个包含大小写字母的字符串。求出由这些字母构成的最长的回文串的长度是多少。
数据是大小写敏感的，也就是说，"Aa" 并不会被认为是一个回文串。
假设字符串的长度不会超过 100000。


样例 1:

输入 : s = "abccccdd"
输出 : 7
说明 : 
一种可以构建出来的最长回文串方案是 "dccaccd"。
'''


class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """

    def longestPalindrome(self, s):
        # write your code here

        hash = {}
        for c in s:
            if c in hash:
                del hash[c]
            else:
                hash[c] = True

        remove = len(hash)
        if remove > 0:
            remove -= 1

        return len(s) - remove


if __name__ == '__main__':
    s = Solution()
    origin = 'sadsd'
    target_length = s.longestPalindrome(origin)
    print(target_length)
