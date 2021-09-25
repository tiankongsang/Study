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
#显示name和year两列
display(df5.loc[:,['name','year']] ) 
#显示北京和上海行中的name和year两列
display(df5.loc[['北京','上海'],['name','year']] ) 
#显示year大于等于2002的name和year信息
display(df5.loc[df5['year']>=2002,['name','year']] )
display(df5)
df5.loc[df5['name'].isin(['李四','小明'])]
df5.loc[df5['year'].isin(['2001','2003'])]