from IPython.display import display
import pandas as pd
data = {
    'name':['张三', '李四', '王五', '小明'],
    'sex':['female', 'female', 'male', 'male'],
    'year':[2001, 2001, 2003, 2002],
    'city':['北京', '上海', '广州', '北京']
}
df = pd.DataFrame(data)
df5 = df.set_index('city')
w1 = df5[['name','year']]
display(w1)
# 选择非‘int64’类型的列显示
display(df5.select_dtypes(exclude='int64').head())
# 选择‘int64’、和‘object’类型的列显示
print(df5.select_dtypes(include=['int64', 'object']).head())