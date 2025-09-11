# WeigConvert.py
WeigStr=input("请输入带有符号的重量值")
if WeigStr.endswith('kg'):
    m=eval(WeigStr[:-2])*2.2046
    print("转换后的重量是{:.2f}pd".format(m))
elif WeigStr.endswith('pd'):
    m=eval(WeigStr[:-2])/2.2046
    print("转换后的重量是{:.2f}kg".format(m))
else:
    print("输入格式错误")# 在这个文件下编写代码，题目具体要求见README.md文件
