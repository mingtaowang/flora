# def get_sub(arrs):
#     res = [arrs[0]]
#     max_sum = arrs[0]  # max sum
#     pre_sum = 0  # pre sum
#     start = 0
#     for index, item in enumerate(arrs):
#         if pre_sum < 0:
#             pre_sum = item
#             start = index
#         else:
#             pre_sum += item
#
#         if pre_sum > max_sum:
#             max_sum = pre_sum
#             res = [arrs[i] for i in range(start, index + 1)]
#
#     return max_sum, res
#
#
# lists = [7, -3, -9, 1, -2, 7, 6, -15, 1, 20, 2, 2]
# lists = [7, -9]
# max_nu, sub = get_sub(lists)
# print(max_nu, sub)

'''
add two big string
'''
# def add_str(num1, num2):
#     res = []
#     idx_1 = len(num1) - 1
#     idx_2 = len(num2) - 1
#     carry = 0
#     while idx_1 >= 0 or idx_2 >= 0:
#         tmp = carry
#         if idx_1 >= 0:
#             tmp += int(num1[idx_1])
#             idx_1 -= 1
#         if idx_2 >= 0:
#             tmp += int(num2[idx_2])
#             idx_2 -= 1
#
#         carry, left = divmod(tmp, 10)
#         res.append(str(left))
#
#     if carry > 0:
#         res.append(str(carry))
#
#     return ''.join(reversed(res))
#
#
# res = add_str('1239328', '45')
# print(res)
'''
1，2，3，4，5，6，7，8，9，10，11，12，13，14
'''

# def find_num(n):
#     if n <= 9:
#         return n
#
#     len = 1
#     count = 9
#     start = 1
#
#     while n > len * count:
#         n -= len * count
#         len += 1
#         count *= 10
#         start *= 10
#
#     start += (n - 1) // len
#     index = (n - 1) % len
#     return int(str(start)[index])
#
#
# num = find_num(191)
# print(num)


'''N皇后'''

# class Solution(object):
#
#     def solve(self, n):
#         self.helper([-1] * n, 0, n)
#
#     def helper(self, position, row_index, n):
#         if row_index == n:
#             self.show_s(position, n)
#             return
#
#         for column in range(n):
#             position[row_index] = column
#             if self.is_valid(position, row_index):
#                 self.helper(position, row_index + 1, n)
#
#     def is_valid(self, position, row_index):
#         if len(set(position[:row_index + 1])) != len(position[:row_index + 1]):
#             return False
#
#         for i in range(row_index):
#             if abs(position[i] - position[row_index]) == int(row_index - i):
#                 return False
#
#         return True
#
#     def show_s(self, position, n):
#         for row in range(n):
#             line = ""
#             for column in range(n):
#                 if position[row] == column:
#                     line += "Q\t"
#                 else:
#                     line += ".\t"
#             print(line, "\n")
#         print('\n')
#
#
# Solution().solve(4)


from itertools import permutations

N = 4
# sol = 0
cols = range(N)
for combo in permutations(cols):
    # print('combo', combo)
    # print(set(combo[i] + i for i in cols))
    # print(set(combo[i] - i for i in cols))
    if N == len(set(combo[i] + i for i in cols)) == len(set(combo[i] - i for i in cols)):
        # sol += 1
        # print('Solution ' + str(sol) + ': ' + str(combo) + '\n')
        print("\n".join(' o ' * i + ' X ' + ' o ' * (N - i - 1) for i in combo) + "\n\n\n\n")
