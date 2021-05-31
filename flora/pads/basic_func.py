import numpy as np
import pandas as pd

# generate Series
s = pd.Series([1, 3, 5, np.nan, 6, 8])
# print(s)

dates = pd.date_range('20130101', periods=6)
# print(dates)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print(df)

df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})
# print(df2)
# print(df2.dtypes)

# 查看头尾数据
# print(df.head())

# 查看尾部数据
# print(df.tail(3))

# 显示索引
# print(df.index)

# 显示列
# print(df.columns)

# nps = df.to_numpy()
# print(nps)

# 可以快速查看数据的统计摘要
# print(df.describe())

# 转置数据
# print(df.T)

# 按轴排序
# df = df.sort_index(axis=1, ascending=True)
# print(df)

# 按值排序
# df = df.sort_values(by='B')
# print(df)

# 获取数据
# print(df['A'])
# print(df[0:3])

# 用标签提取一行
# print(df.loc[dates[0]])

# 用标签选择多列
# print(df.loc[:, ['A', 'B']])

# 用标签切，包含行与列结束点
# print(df.loc['20130102':'20130104', ['A', 'B']])

# 返回对象降维
# print(df.loc['20130102', ['A', 'B']])

# 提取标量值
# print(df.loc[dates[0], 'A'])

# 快速访问标量
# print(df.at[dates[0], 'A'])

# 用整数位置选择
# print(df.iloc[3])

# 用整数切片
# print(df.iloc[3:5, 0:2])

# 用整数列表按位置切片
# print(df.iloc[[1, 2, 4], [0, 2]])

# 显式整行切片
# print(df.iloc[1:3, :])

# 显式整列切片
# print(df.iloc[:, 1:3])

# 快速访问标量
# print(df.iat[1, 1])

# 布尔索引