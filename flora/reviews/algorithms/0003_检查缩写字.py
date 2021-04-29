desc = '''
给定一个非空字符串 word 和缩写 abbr，返回字符串是否可以和给定的缩写匹配。
比如一个 “word” 的字符串仅包含以下有效缩写：
["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]


样例 1:

输入 : s = "internationalization", abbr = "i12iz4n"
输出 : true

样例 2:

输入 : s = "apple", abbr = "a2e"
输出 : false
'''


class Solution:
    """
    @param word: a non-empty string
    @param abbr: an abbreviation
    @return: true if string matches with the given abbr or false
    """
    def validWordAbbreviation(self, word, abbr):
        # write your code here
        i, j = 0, 0
        while i < len(abbr) and j < len(word):
            if abbr[i].isdigit():
                if abbr[i] == '0':
                    return False

                gram_len = 0
                while i < len(abbr) and abbr[i] in '0123456789':
                    gram_len = gram_len * 10 + int(abbr[i])
                    i += 1

                j += gram_len
            else:
                if abbr[i] != word[j]:
                    return False

                i += 1
                j += 1

        return i == len(abbr) and j == len(word)


if __name__ == '__main__':
    s = Solution()
    word = 'apple'
    abbr = 'a2e'
    res = s.validWordAbbreviation(word, abbr)
    print(res)
