desc = '''
判断符号是否成对出现，并且嵌套正确
其中'('与')'、‘{’与'}'、‘[’与']'、‘<’与‘>’、‘《’与‘》’为成对的符号
'''


class Solution:

    def is_valid_str(self, ss):
        patterns = {')': '(', '}': '{', ']': '[', '>': '<', '》': '《'}
        res = []
        for item in ss:
            if item in patterns.values():
                res.append(item)
            elif item in patterns.keys():
                if res == [] or res.pop() != patterns.get(item):
                    return False
            else:
                return False
        return res == []


if __name__ == '__main__':
    s = Solution()
    ss = 'a[{}]'
    res = s.is_valid_str(ss)
    print(res)
