desc = '''
a可以表示成a = kb + r（a，b，k，r皆为正整数，且r < b），则r = a mod b
假设d是a,b的一个公约数,r = a - kb
两边同时除以d，r/d=a/d-kb/d=m，m为整数
因此，d是b的公约数，d是a%b的公约数，d是a的公约数
（a, b）(b, a % b)的公约数是一样的，其最大公约数也必然相等
'''


class Solution:

    def gcd(self, a, b):
        a = max(a, b)
        b = min(a, b)
        if a % b == 0:
            return b

        return self.gcd(b, a % b)


if __name__ == '__main__':
    s = Solution()
    a = 15
    b = 12
    res = s.gcd(a, b)
    print(res)
