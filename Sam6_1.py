user_input = input("Введите последовательность чисел, разделённых пробелом: ")

string_numbers = user_input.split()

try:
    integer_list = [int(num) for num in string_numbers]
except ValueError:
    print("Ошибка: Введены некорректные данные. Пожалуйста, введите только числа.")
    exit()

integer_tuple = tuple(integer_list)

print(f"Список: {integer_list}")
print(f"Кортеж: {integer_tuple}")
