def calculate_structure_sum(data):
    total_sum = 0

    def process_data(item):
        nonlocal total_sum

        if isinstance(item, int):
            total_sum += item
        elif isinstance(item, str):
            total_sum += len(item)
        elif isinstance(item, list) or isinstance(item, tuple):
            for subitem in item:
                process_data(subitem)
        elif isinstance(item, dict):
            for key, value in item.items():
                process_data(key)
                process_data(value)

    process_data(data)

    return total_sum


# Входные данные (применение функции)
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)