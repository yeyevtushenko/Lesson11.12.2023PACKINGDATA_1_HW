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

def print_menu():
    print("\nОберіть опцію:")
    print("1. Додати країну")
    print("2. Видалити країну")
    print("3. Пошук країни")
    print("4. Редагувати країну")
    print("5. Зберегти дані")
    print("6. Завантажити дані")
    print("0. Вийти")

if __name__ == "__main__":
    capitals_dict = load('capitals.json.gz')

    while True:
        print_menu()
        choice = input("Ваш вибір: ")

        if choice == "1":
            country = input("Введіть назву країни: ")
            capital = input("Введіть назву столиці: ")
            add(capitals_dict, country, capital)

        elif choice == "2":
            country = input("Введіть назву країни для видалення: ")
            remove(capitals_dict, country)

        elif choice == "3":
            country = input("Введіть назву країни для пошуку: ")
            search(capitals_dict, country)

        elif choice == "4":
            country = input("Введіть назву країни для редагування: ")
            new_capital = input("Введіть нову назву столиці: ")
            edit(capitals_dict, country, new_capital)

        elif choice == "5":
            save(capitals_dict, 'capitals_updated.json.gz')

        elif choice == "6":
            capitals_dict = load('capitals_updated.json.gz')

        elif choice == "0":
            break

        else:
            print("Невірний вибір. Будь ласка, виберіть іншу опцію.")










