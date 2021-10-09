import pandas as pd
import numpy as np

tu = {'name': ['小明', '王芳', '赵平', '李红', '李涵'],
      'sex': ['male', 'female', 'female', 'female', 'male'],
      'year': [1996, 1997, 1994, 1999, 1996]}
data = pd.DataFrame(stu)
print(data['sex'].value_counts())
print(data['sex'].value_counts().plot(kind='bar', rot=30))
