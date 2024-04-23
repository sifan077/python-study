# 写模式，如果文件不存在，会自动创建
f = open('data.txt', 'w',encoding='utf-8')
f.write('hello world2')
# 把内存中的内容写入到磁盘，刷新缓冲区
f.flush()
f.close()

# 追加模式
f = open('data.txt', 'a',encoding='utf-8')
for i in range(1,15):
    f.write('hello world{}\n'.format(i))
f.close()

