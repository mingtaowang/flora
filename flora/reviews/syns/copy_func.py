import copy

# a = [1, 2, 3, 4, ['a', 'b']]
#
# b = a
# c = copy.copy(a)
# d = copy.deepcopy(a)
#
# a.append(5)
# a[4].append('c')

a = [1, 2, 3]
b = [a, a]
temp = copy.deepcopy(b)
c = id(b[0]) == id(temp[0])
d = id(b[0]) == id(b[1])

if __name__ == '__main__':
    # a: [1, 2, 3, 4, ['a', 'b', 'c'], 5]
    # b: [1, 2, 3, 4, ['a', 'b', 'c'], 5]
    # c: [1, 2, 3, 4, ['a', 'b', 'c']]
    # d: [1, 2, 3, 4, ['a', 'b']]

    # a: [1,2,3]
    # b: [[1,2,3],[1,2,3]]
    # c: False
    # c: True
    print(a)
    print(b)
    print(c)
    print(d)
