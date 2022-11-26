list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
pos_in_list = 0  # Переменная положения элемента в списке
max_last_value = list_numbers[pos_in_list]  # Переменная значения элемента в списке
# TODO Оформить решение
for pos, value in enumerate(list_numbers):  # Перебор пар Позиция - Значение
    if value >= max_last_value:  # Находим позицию и значение последнего максимального элемента
        pos_in_list = pos
        max_last_value = value
# Заменяем значения в списке
list_numbers[pos_in_list], list_numbers[-1] = list_numbers[-1], list_numbers[pos_in_list]
print(list_numbers)  # Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]
