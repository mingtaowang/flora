desc = '''
最初，机器人位于(0, 0)处。 给定一系列动作，判断该机器人的移动轨迹是否是一个环，这意味着它最终会回到原来的位置。

移动的顺序由字符串表示。 每个动作都由一个字符表示。 有效的机器人移动是R（右），L（左），U（上）和D（下）。 输出应该为true或false，表示机器人是否回到原点。


样例1:

输入: "UD"
输出: true

样例2:

输入: "LL"
输出: false
'''


class Solution:
    """
    @param moves: a sequence of its moves
    @return: if this robot makes a circle
    """
    def judgeCircle(self, moves):
        # Write your code here
        if len(moves) < 2:
            return False

        i = 0
        j = 0
        for item in moves:
            if item == 'R':
                j += 1
            elif item == 'L':
                j -= 1
            elif item == 'U':
                i -= 1
            elif item == 'D':
                i += 1
            else:
                pass

        return True if not i and not j else False


if __name__ == '__main__':
    s = Solution()
    origin = "UD"
    res = s.judgeCircle(origin)
    print(res)
