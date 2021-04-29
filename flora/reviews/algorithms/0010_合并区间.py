desc = '''
给出若干闭合区间，合并所有重叠的部分。


样例1:

输入: [(1,3)]
输出: [(1,3)]

样例 2:

输入:  [(1,3),(2,6),(8,10),(15,18)]
输出: [(1,6),(8,10),(15,18)]
'''

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    @param intervals: interval list.
    @return: A new interval list.
    """

    # def merge(self, intervals):
       ## 网站上好使的
    #     intervals = sorted(intervals, key=lambda x: x.start)
    #     result = []
    #     for interval in intervals:
    #         if len(result) == 0 or result[-1].end < interval.start:
    #             result.append(interval)
    #         else:
    #             result[-1].end = max(result[-1].end, interval.end)
    #     return result

    def merge(self, intervals):
        # python好使的
        intervals = sorted(intervals, key=lambda x: x[0])
        intervals = [list(item) for item in intervals]
        result = [intervals[0]]
        for interval in intervals[1:]:
            if result[-1][-1] < interval[0]:
                result.append(interval)
            else:
                result[-1][-1] = max(result[-1][-1], interval[1])
        return [tuple(i) for i in result]


if __name__ == '__main__':
    s = Solution()
    origin = [(1, 3), (2, 6), (8, 10), (15, 18)]
    origin = [(1, 4), (1, 4)]
    res = s.merge(origin)
    print(res)
