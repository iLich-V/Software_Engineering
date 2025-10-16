def get_office_sequence(tuple_data, employee_id):
    if employee_id not in tuple_data:
        return ()

    first_index = tuple_data.index(employee_id)

    try:
        second_index = tuple_data.index(employee_id, first_index + 1)
        return tuple_data[first_index:second_index + 1]
    except ValueError:
        return tuple_data[first_index:]

test_cases = [
    ((1, 2, 3), 8),
    ((1, 8, 3, 4, 8, 8, 9, 2), 8),
    ((1, 2, 8, 5, 1, 2, 9), 8)
]

sources = []
results = []

for tuple_data, emp_id in test_cases:
    result = get_office_sequence(tuple_data, emp_id)
    sources.append(f"{tuple_data, emp_id}")
    results.append(f"{result}")

for source in sources:
    print(source)
print()
for result in results:
    print(result)
