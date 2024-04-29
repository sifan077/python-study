# 递归，需要满足两个条件：1. 有终止条件 2. 递归调用自身

import os


def list_folder(path) -> list:
    file_list = []
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            file_list.extend(list_folder(file_path))
        else:
            file_list.append(file_path)
    return file_list


print(len(list_folder('D:\\其他\\1\\李志')))
