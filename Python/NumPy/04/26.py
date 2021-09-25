import pandas as pd
data = {
    'name':['张三', '李四', '王五', '小明'],
    'sex':['female', 'female', 'male', 'male'],
    'year':[2001, 2001, 2003, 2002],
    'city':['北京', '上海', '广州', '北京']
}
df = pd.DataFrame(data)
print(df)
print('显示前2行:\n',df[:2])  
print('显示2-3两行:\n',df[1:3])  