import re

s = 'python itcast sifan xiaoyue itcast'
# 匹配字符串开头
result = re.match('itcast', s)
print(result)

# 匹配字符串 anywhere
result = re.search('itcast', s)
print(result)

# 匹配所有字符串 anywhere
result = re.findall('itcast', s)
print(result)

# 元字符匹配

# 匹配数字
result = re.findall('\d', 'abc123')
print(result)

# 匹配字母
result = re.findall('[a-z]', 'abc123')
print(result)

# 匹配字母或数字
result = re.findall('[a-z0-9]', 'abc123')
print(result)

# 匹配字母或数字或下划线
result = re.findall('[a-z0-9_]', 'abc123')
print(result)
# 匹配字母或数字或下划线或空格
result = re.findall('[a-z0-9_ ]', 'abc123')
print(result)

# 匹配账号，只能由数字和字母组成，且长度在6-16之间
result = re.findall('[a-z0-9A-Z]{6,16}', 'AAAabc123')
print(result)

# 匹配邮箱
result = re.findall('$\w+@\w+.\w+^', 'gh66544@163.com')
print(result)

# 匹配所有单词
result = re.findall('\w+', 'Hello World , This a gift')
print(result)

# 匹配qq,5-10位数字,首位不为0
result = re.findall('$[1-9]\d{4,9}^', '1234567891110')
print(result)
