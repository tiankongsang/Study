import pandas as pd

data = {
    'name': ['张三', '李四', '王五', '小明'],
    'sex': ['female', 'female', 'male', 'male'],
    'year': [2001, 2001, 2003, 2002],
    'city': ['北京', '上海', '广州', '北京']
}
df = pd.DataFrame(data)
print(df)
print('信息表的所有值为：\n', df.values)
print('信息表的所有列为：\n', df.columns)
print('信息表的元素个数为：\n ', df.size)
print('信息表的维度是\n ', df.ndim)
print('信息表的形状为：', df.shape)
