import pandas as pd

data = {
    'name': ['张三', '李四', '王五', '小明'],
    'sex': ['female', 'female', 'male', 'male'],
    'year': [2001, 2001, 2003, 2002],
    'city': ['北京', '上海', '广州', '北京']
}
df = pd.DataFrame(data)
df5 = df.set_index('city')
# df5['age'] = 20
# df5['C'] = [85,78,96,80]
# print(df5)
df5['score'] = [85, 78, 96, 80]
df5.insert(1, 'no', ['001', '002', '003', '004'])
print(df5)
