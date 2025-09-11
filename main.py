# 公制千克与英制磅转换程序
weight_str = input("请输入带有符号的重量值（例如 10kg 或 10pd）：")

if weight_str.endswith("kg"):
    # 提取数值部分并转换为浮点数
    kg = float(weight_str[:-2])
    # 千克转磅，1 千克 = 2.2046 磅
    pounds = kg * 2.2046
    # 保留 3 位小数
    print(f"转换后的重量是{pounds:.3f}pd")
elif weight_str.endswith("pd"):
    # 提取数值部分并转换为浮点数
    pd = float(weight_str[:-2])
    # 磅转千克，1 磅 = 1 / 2.2046 千克
    kilograms = pd / 2.2046
    # 保留 3 位小数
    print(f"转换后的重量是{kilograms:.3f}kg")
else:
    print("输入格式错误，请输入如 10kg 或 10pd 格式的重量值")

# 测试输入 10kg 的情况
# 输入：10kg
# 输出：转换后的重量是22.046pd

# 测试输入 10pd 的情况
# 输入：10pd
# 输出：转换后的重量是4.535kg
