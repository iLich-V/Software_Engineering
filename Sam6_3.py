def count_top_three(digits_string):
    count_dict = {}

    for char in digits_string:
        digit = int(char)
        count_dict[digit] = count_dict.get(digit, 0) + 1

    top_three = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))[:3]

    result_dict = dict(top_three)
    sorted_result = dict(sorted(result_dict.items()))
    return result_dict, sorted_result

digits = input(f"Введите число: ")
result, sorted_result = count_top_three(digits)

print("Словарь 3-х самых частых чисел:", result)
print("Отсортированный по возрастанию ключа:", sorted_result)
