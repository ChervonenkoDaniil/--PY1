def delete(list_, index=None):
    # используем cпособ list comprehension
    list_ = (list_[:-1] if index is None else list_[:index] + list_[index + 1:])
    return list_


# TODO реализовать функцию удаления элемента из списка по индексу


print(delete([0, 1, 2], index=0))  # [0, 1], ошибка, правильно [1,2]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]
