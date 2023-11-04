import string

def replace_punctuation_with_space(input_string):
    # 创建一个标点符号字符集
    punctuation = string.punctuation

    # 使用str.replace()方法将标点符号替换为空格
    cleaned_string = input_string
    for char in punctuation:
        cleaned_string = cleaned_string.replace(char, ' ')

    return cleaned_string

# 获取用户输入
user_input = input("请输入一个字符串: ")

# 调用函数替换标点符号
result = replace_punctuation_with_space(user_input)

# 打印替换后的字符串
print(result)
