import pandas as pd

data = {
    'name': ['张三', '李四', '王五', '小明'],
    'sex': ['female', 'female', 'male', 'male'],
    'year': [2001, 2001, 2003, 2002],
    'city': ['北京', '上海', '广州', '北京']
}
df = pd.DataFrame(data)
df5 = df.set_index('city')
data1 = {'city': '兰州', 'name': '李红', 'year': 2005, 'sex': 'female'}
print(df5.append(data1, ignore_index=True))
