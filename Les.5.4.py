some_list = list(range(0, 20))

print(some_list)

for i in range(len(some_list)):

    if some_list[i] % 2 != 0:

        some_list[i] = 0

print(some_list)

print(some_list.count(0))