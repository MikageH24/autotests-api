import json


json_data_str = '''{
  "name": "Иван",
  "age": 30,
  "is_student": false,
  "courses": ["Python", "QA Automation", "API Testing"],
  "address": {
    "city": "Москва",
    "zip": "101000"
  }
}'''

# Загрузка JSON (парсинг)
# Преобразуем JSON-строку в Python-объект (dict)
file = json.loads(json_data_str)
print(file, type(file))

json_data_dict = {
  "name": "Иван",
  "age": 30,
  "is_student": False,
  "courses": ["Python", "QA Automation", "API Testing"],
  "address": {
    "city": "Москва",
    "zip": "101000"
  }
}

# Сохранение JSON (сериализация)
# Преобразуем Python-объект в JSON-строку
file1 = json.dumps(json_data_dict, indent=4, ensure_ascii=False)
print(file1, type(file1))


# Загружаем JSON из файла, dict
with open("json.json", "r", encoding="utf-8") as file2:
    data = json.load(file2)
    print(data)

with open("json_new.json", "w", encoding="utf-8") as new_file:
    json.dump(json_data_dict, new_file, ensure_ascii=False, indent=2)

