desc = '''
一棵二叉树，找出从根节点到叶子节点的所有路径。


样例 1:

输入：{1,2,3,#,5}
输出：["1->2->5","1->3"]
解释：
   1
 /   \
2     3
 \
  5
  
样例 2:

输入：{1,2}
输出：["1->2"]
解释：
   1
 /   
2
'''


class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """

    def binaryTreePaths(self, root):
    # write your code here
        return []


if __name__ == '__main__':
    s = Solution()
    origin = {1, 2, 3, '#', 5}
    res = s.binaryTreePaths(origin)
    print(res)
