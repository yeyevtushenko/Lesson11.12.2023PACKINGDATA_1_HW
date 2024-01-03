import json
import gzip

def add(capitals, country, capital):
    capitals[country] = capital
    print(f"Додано: {country} - {capital}")

def remove(capitals, country):
    if country in capitals:
        del capitals[country]
        print(f"Видалено: {country}")
    else:
        print(f"Країна {country} не знайдена")

def search(capitals, country):
    if country in capitals:
        print(f"Столиця {country}: {capitals[country]}")
    else:
        print(f"Країна {country} не знайдена")

def edit(capitals, country, new_capital):
    if country in capitals:
        capitals[country] = new_capital
        print(f"Змінено: {country} - {new_capital}")
    else:
        print(f"Країна {country} не знайдена")

def save(capitals, filename):
    with gzip.open(filename, 'wt', encoding='utf-8') as file:
        json.dump(capitals, file)
        print(f"Дані збережено у файлі: {filename}")

def load(filename):
    try:
        with gzip.open(filename, 'rt', encoding='utf-8') as file:
            capitals = json.load(file)
            print(f"Дані завантажено з файлу: {filename}")
            return capitals
    except FileNotFoundError:
        print(f"Файл {filename} не знайдено. Створено новий порожній словник.")
        return {}










