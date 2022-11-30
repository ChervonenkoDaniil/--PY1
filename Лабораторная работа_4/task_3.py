def delete(list_, index=-1):
    if index == -1:
        list_ = list_[:index]
    else:
        list_ = list_[:index] + list_[index+1:]
    return list_

# TODO реализовать функцию удаления элемента из списка по индексу


print(delete([0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]
