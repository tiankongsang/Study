from IPython.display import display
import pandas as pd

data = {
    'name': ['张三', '李四', '王五', '小明'],
    'sex': ['female', 'female', 'male', 'male'],
    'year': [2001, 2001, 2003, 2002],
    'city': ['北京', '上海', '广州', '北京']
}
df = pd.DataFrame(data)
df5 = df.set_index('city')
df5.drop('广州', inplace=True)
display(df5)
# 删除数据的列
df5.drop('sex', axis=1, inplace=True)
display(df5)
df5.replace('张三', '小王', inplace=True)
display(df5)
