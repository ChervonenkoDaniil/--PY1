import json


INPUT_FILE = "input.csv"


# Очень долго думал, но не придумал, зачем функция воспринимает аргумент разделителя, но, по заданию добавил
def csv_to_list_dict(filename, delimiter=',', new_line='\n') -> list[dict]:
    # Получаем данные, форматируем для дальнейшей работы
    with open(filename, 'r') as f:
        headers = f.readline().split(delimiter)
        data = f.readlines()
        data = [i.split(delimiter) for i in data]
    # Вероятнее всего, для удаления из конца строки, но не понял, как реализовать
    headers[-1] = headers[-1].strip()

    for line in data:
        line[-1] = line[-1].strip()
    # Объединяем в словарь
    dict_ = [dict(zip(headers, [i for i in line])) for line in data]
    return dict_


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
