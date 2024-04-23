f1 = open('./data.txt', 'r', encoding='utf-8')
lines = f1.readlines()
f1.close()
f2 = open('./data.txt.bak', 'w', encoding='utf-8')
for line in lines:
    if line.__contains__("正式"):
        line.strip()
        f2.write(line)
        f2.flush()
f2.close()
