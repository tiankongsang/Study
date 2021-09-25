import pandas as pd
df = pd.DataFrame({'price': [1.99, 3, 5, 0.5, 3.5, 5.5, 3.9]})
print(df[(df.price >= 2) & (df.price <= 4)])
# 或者使用between实现，df[df.price.between(2, 4)]