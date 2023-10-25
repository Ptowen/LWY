# 输入一个正整数
num = int(input("请输入一个正整数："))

# 计算该整数的平方
square = num ** 2

# 将整数和平方数转换为字符串，以便进行字符串操作
num_str = str(num)
square_str = str(square)

# 判断是否是同构数
if square_str.endswith(num_str):
    print(f"{num} 是一个同构数")
else:
    print(f"{num} 不是一个同构数")
5