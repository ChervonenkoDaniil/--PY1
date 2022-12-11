from random import choice


def get_unique_list_numbers(start=-10, stop=10, n=15) -> list[int]:  # Добавлено для универсальности решения
    list_of_numbers = []  # Создаем список для заполнения
# Цикл while, т.к устанавливаем четкие границы работы цикла c выполнением условия отсутствия повтора чисел в списке
# При использовании цикла for, цикл продолжался, теряя позиции в списке при повторе переменной number
    while len(list_of_numbers) != n:
        number = randint(start, stop)  # Вызываем случайное число из интервала
        if number not in list_of_numbers:
            list_of_numbers.append(number)
    return list_of_numbers
# TODO написать функцию для получения списка уникальных целых чисел


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
