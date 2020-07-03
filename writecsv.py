import pandas as pd
import numpy as np

'''第二种写法：当值为string类型的数据，此时需要加上 index=[0] 因为pandas 的dataframe需要一个可迭代的对象'''
data2 = {'姓名': 'fuhang', '性别': '男', '昵称': '那时的吻真香'}
df2=pd.DataFrame(data2,index=[0])
df2.to_csv('Result2.csv',index=None)

#df1.to_csv('Result1.csv',index=None,mode='a')　
