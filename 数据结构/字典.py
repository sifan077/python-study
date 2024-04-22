# 定义空字典
empty_dic1 = {}
print(empty_dic1)
empty_dic2 = dict()
print(empty_dic2)

# 定义一个字典,key value,可以理解为Map集合
dic = {'name': '小明', 'age': 18, 'gender': '男'}
print(dic)

# 如果存在键,则更新值,不存在则添加
dic['age'] = 20
dic['address'] = '北京'
print(dic)

# 删除键
dic.pop("address")
print(dic)

# 获取全部的key
print(dic.keys())

# 获取数量
print(len(dic))

# 遍历字典的key
for key in dic:
    print(f'{key}: {dic[key]}')

for k, v in dic.items():
    print(f'{k}: {v}')
