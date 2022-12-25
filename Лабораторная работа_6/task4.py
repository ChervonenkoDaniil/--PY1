import json


INPUT_FILE = "input.csv"


# Нашел применение для new_line, удалил лишние строки
def csv_to_list_dict(filename, delimiter=',', new_line='\n') -> list[dict]:
    # Получаем список заголовков, форматируем для дальнейшей работы (с удалением \n)
    with open(filename, 'r') as f:
        headers = f.readline().strip(new_line).split(delimiter)
        # Выводим словарь для экспорта
        return [dict(zip(headers, line.strip(new_line).split(delimiter))) for line in f.readlines()]


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
