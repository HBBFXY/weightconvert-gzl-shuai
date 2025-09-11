# WeigConvert.py
WeigStr = input("请输入带有符号的重量值")
if WeigStr.endswith('kg'):
    # 提取数值部分并转为浮点数
    num = float(WeigStr[:-2])
    # 千克转磅（1kg ≈ 2.2046磅）
    pounds = num * 2.2046
    # 截断到3位小数：先×1000取整（截断小数），再÷1000
    truncated_pounds = int(pounds * 1000) / 1000
    print(f"转换后的重量是{truncated_pounds}pd")
elif WeigStr.endswith('pd'):
    # 提取数值部分并转为浮点数
    num = float(WeigStr[:-2])
    # 磅转千克（1磅 ≈ 1/2.2046 kg）
    kilograms = num / 2.2046
    # 截断到3位小数
    truncated_kilograms = int(kilograms * 1000) / 1000
    print(f"转换后的重量是{truncated_kilograms}kg")
else:
    print("输入格式错误")
