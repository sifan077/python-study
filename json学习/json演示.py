import json

data = [
    {"name": "张三", "age": 18, },
    {"name": "李四", "age": 20, },
    {"name": "王五", "age": 22, },
    {"name": "赵六", "age": 24, },
    {"name": "孙七", "age": 26, },
    {"name": "周八", "age": 28, },
    {"name": "吴九", "age": 30, },
    {"name": "郑十", "age": 32, },
    {"name": "王十一", "age": 34, },
    {"name": "赵十二", "age": 36, },

]
# 如果需要中文，需要设置ensure_ascii=False
json_str = json.dumps(data, ensure_ascii=False)
print(json_str)
print(type(json_str))

# 准备字典,把字典转换为json字符串
dic = {
    "name": "张三",
    "age": 18,
    "sex": "男",
    "hobby": ["吃饭", "睡觉", "打豆豆"]
}
json_str = json.dumps(dic, ensure_ascii=False)
print(json_str)

# 把字符串转换为列表
data_str = '[{"name": "张三", "age": 18}, {"name": "李四", "age": 20}, {"name": "王五", "age": 22}, {"name": "赵六", "age": 24}, {"name": "孙七", "age": 26}, {"name": "周八", "age": 28}, {"name": "吴九", "age": 30}, {"name": "郑十", "age": 32}, {"name": "王十一", "age": 34}, {"name": "赵十二", "age": 36}]'
data = json.loads(data_str)
print(data)
print(type(data))

# 把字符串转换为字典
dic_str = '{"name": "张三", "age": 18, "sex": "男", "hobby": ["吃饭", "睡觉", "打豆豆"]}'
dic = json.loads(dic_str)
print(dic)
print(type(dic))
