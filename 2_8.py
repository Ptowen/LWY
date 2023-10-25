# 导入math模块以使用math.gcd函数
import math

# 输入两个整数
num1 = int(input("请输入第一个整数："))
num2 = int(input("请输入第二个整数："))

# 计算最大公约数
gcd = math.gcd(num1, num2)

# 计算最小公倍数
lcm = (num1 * num2) // gcd

# 输出结果
print(f"{num1} 和 {num2} 的最小公倍数是 {lcm}")
