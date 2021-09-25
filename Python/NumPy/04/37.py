import pandas as pd
data = {'fruit':['apple','grape','banana'],'price':['30元','43元','28元']}
df1 = pd.DataFrame(data)
print(df1)
def f(x):
    return x.split('元')[0]
df1['price'] = df1['price'].map(f)
print('修改后的数据表:\n',df1)
