import random

def create_demo_lists(list_length, num_lists, min_value, max_value):
    demo_lists = []

    for _ in range(num_lists):
        new_list = [random.randint(min_value, max_value) for _ in range(list_length)]
        demo_lists.append(new_list)

    return demo_lists

list_length = int(input("Enter the length of each list: "))
num_lists = int(input("Enter the number of lists: "))
min_value = int(input("Enter the minimum value for elements: "))
max_value = int(input("Enter the maximum value for elements: "))

result_lists = create_demo_lists(list_length, num_lists, min_value, max_value)

print("Demo Lists:")
for demo_list in result_lists:
    print(demo_list)