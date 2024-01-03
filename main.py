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







