desc = '''
给一个 01 矩阵，求不同的岛屿的个数。

0 代表海，1 代表岛，如果两个 1 相邻，那么这两个 1 属于同一个岛。我们只考虑上下左右为相邻。


样例 1：

输入：
[
  [1,1,0,0,0],
  [0,1,0,0,1],
  [0,0,0,1,1],
  [0,0,0,0,0],
  [0,0,0,0,1]
]
输出：
3

样例 2：

输入：
[
  [1,1]
]
输出：
1
'''


class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
    # write your code here
        if not grid or not grid[0]:
            return 0

        n = len(grid)
        m = len(grid[0])
        lands = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    lands += 1
                    self.change(grid, i, j)

        return lands

    def change(self, grid, i, j):
        grid[i][j] = 0

        # 上方
        if i > 0 and grid[i - 1][j] == 1:
            self.change(grid, i - 1, j)

        # 左方
        if j > 0 and grid[i][j - 1] == 1:
            self.change(grid, i, j - 1)

        # 下方
        if i < len(grid) - 1 and grid[i + 1][j] == 1:
            self.change(grid, i + 1, j)

        # 右方
        if j < len(grid[0]) - 1 and grid[i][j + 1] == 1:
            self.change(grid, i, j + 1)


if __name__ == '__main__':
    s = Solution()
    grid = [
        [1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1]
    ]
    res = s.numIslands(grid)
    print(res)
