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






