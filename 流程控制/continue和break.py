for i in range(1, 10):
    if i % 2 == 0:
        continue
    print(i, end=" ")

print()
for i in range(1, 10):
    if i % 5 == 0:
        break
    print(i, end=" ")
