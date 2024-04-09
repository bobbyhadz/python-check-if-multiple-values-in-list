# Check if multiple values are in a list in Python

my_list = ['one', 'two', 'three', 'four', 'five']

multiple_values = ['one', 'two', 'three']

if all(value in my_list for value in multiple_values):
    # 👇️ this runs
    print('All of the values are in the list')
else:
    print('Not all of the values are in the list')

# 👇️ True
print(all(value in my_list for value in multiple_values))