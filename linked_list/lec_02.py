import sys

my_list = []
print(f"Length: {len(my_list)}, Size in bytes: {sys.getsizeof(my_list)}")

for i in range(100):
    my_list.append(i)
    print(f"Length: {len(my_list)}, Size in bytes: {sys.getsizeof(my_list)}")
