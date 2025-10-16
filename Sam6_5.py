def calculate_average_score(scores: list) -> float:
    """
    Рассчитывает средний балл на основе списка оценок.
    """
    if not scores:
        return 0.0

    total_sum = sum(scores)
    count = len(scores)

    average = total_sum / count

    return average

# Тест 1: Смешанные оценки
test_scores_1 = [5, 4, 4, 5, 3]
result_1 = calculate_average_score(test_scores_1)
print(f"Тест 1. Оценки: {test_scores_1}")
print(f"Результат: {result_1}. Ожидаемый: 4.2. {'Успех' if result_1 == 4.2 else 'Ошибка'}")

# Тест 2: Идеальные оценки
test_scores_2 = [5, 5, 5]
result_2 = calculate_average_score(test_scores_2)
print(f"\nТест 2. Оценки: {test_scores_2}")
print(f"Результат: {result_2}. Ожидаемый: 5.0. {'Успех' if result_2 == 5.0 else 'Ошибка'}")

# Тест 3: Пустой список (граничный случай)
test_scores_3 = []
result_3 = calculate_average_score(test_scores_3)
print(f"\nТест 3. Оценки: {test_scores_3}")
print(f"Результат: {result_3}. Ожидаемый: 0.0. {'Успех' if result_3 == 0.0 else 'Ошибка'}")
