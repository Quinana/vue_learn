import math
import matplotlib.pyplot as plt
# import numpy as np
import pandas as pd
import openpyxl
import numpy as np

# generate random num tested
src_data = pd.read_excel(r'C:\Users\钟其洋\Desktop\test1\网眼.xlsx',sheet_name=0,header=0) # 第一张表格，第一行为列名
# pd.set_option('display.max_rows', src_data.shape[0] + 1)
mydata=src_data['Area'].values;

median=np.median(mydata)
print(median)

drop_indices = []
for index, row in src_data.iterrows():
    tmp = row['Area']< 0.1 * median
    if tmp.any():
        drop_indices.append(index)
        
'''for index, row in src_data.iterrows():
    tmp = row['BendHeight'] > 10 * median
    if tmp.any():
        drop_indices.append(index)
'''     

dst_data = src_data.drop(drop_indices)
# print(src_data)
writer = pd.ExcelWriter('网眼.xlsx')
dst_data.to_excel(writer, 'page_1')
writer.save()
