'''
n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击
皇后彼此不能相互攻击，也就是说：任何两个皇后都不能处于同一条横行、纵行或斜线上
'''
from itertools import permutations


class Solution:

    def solve_queens(self, n):
        row = range(n)
        cols = permutations(row)
        for col in cols:
            # 能形成斜对角的坐标，必须x和y相加为固定值或者x-y为固定值
            if len(set(col[i] + i for i in row)) == n and len(set(col[i] - i for i in row)) == n:
                print(col)
                print('\n'.join([' o ' * item + ' x ' + ' o ' * (n - item - 1) for item in col]) + '\n\n\n\n')


if __name__ == '__main__':
    s = Solution()
    n = 5
    s.solve_queens(n)
