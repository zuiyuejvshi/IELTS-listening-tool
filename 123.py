import pandas as pd
import os

# 读取Excel文件
excel_file = r"C:\Users\admin\Desktop\fault.xlsx"
df = pd.read_excel(excel_file, usecols="A")  # 只读取A列

# 自动生成一个txt文件名
txt_file = 'output.txt'

# 将A列内容从第二行开始写入txt文件
with open(txt_file, 'w', encoding='utf-8') as f:
    for item in df.iloc[1:, 0]:  # 从第二行开始遍历A列的每一行
        f.write(str(item) + '\n')  # 每一行写入txt文件

print(f"A列内容已成功写入 {txt_file}")
