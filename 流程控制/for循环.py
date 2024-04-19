# name = 'zhangsanasklhfklashjfklashjfklaskhflashklf'
# count = 0
# for i in name:
#     if i == 'a':
#         count += 1
# print(count)


# range(start,stop,step)
# for i in range(1, 10, 2):
#     print(i, end=' ')
#
# print()
# for i in range(10):
#     print(i, end=' ')
#
# print()
# for i in range(1, 10):
#     print(i, end=' ')


for i in range(1, 10):
    for j in range(1, i + 1):
        print("{}*{}={}\t".format(j, i, j * i),end=" ")
    print()
