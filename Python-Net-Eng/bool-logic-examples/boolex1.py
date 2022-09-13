my_number_of_paths = [1, 1, 1, 1, 1, 1, 1]
my_multipath_list = []

for paths in my_number_of_paths:
    if paths > 1:
        my_multipath_list.append(paths)

if my_multipath_list:
    print(my_multipath_list)
else:
    print("There is no multipath values")
