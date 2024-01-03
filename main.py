import json
import gzip

def add(library, group, albums):
    if group not in library:
        library[group] = albums
    else:
        print(f"Група  {group} вже є у бібліотеці.")

def remove(library, group):
    if group in library:
        del library[group]
    else:
        print(f"Групи {group} немає у бібліотеці.")

def search(library, group):
    return library.get(group, "Група не знайдена у бібліотеці.")

def edit(library, group, new_albums):
    if group in library:
        library[group] = new_albums
    else:
        print(f"Групи {group} немає у бібліотеці.")

def save(library, filename):
    with gzip.open(filename, 'wt') as file:
        json.dump(library, file)

def load(filename):
    with gzip.open(filename, 'rt') as file:
        return json.load(file)

music_library = {}

while True:
    print("\nМеню:")
    print("1. Додати групу та альбоми")
    print("2. Видалити групу")
    print("3. Пошук групи")
    print("4. Редагувати альбоми групи")
    print("5. Зберегти у файл")
    print("6. Завантажити з файлу")
    print("0. Вийти")

    choice = input("Введіть свій вибір: ")

    if choice == "1":
        group = input("Введіть назву групи: ")
        albums = input("Введіть альбоми (розділені комою): ").split(',')
        add(music_library, group, albums)

    elif choice == "2":
        group = input("Введіть назву групи для видалення: ")
        remove(music_library, group)

    elif choice == "3":
        group = input("Введіть назву групи для пошуку: ")
        search_result = search(music_library, group)
        print("Search Result:", search_result)

    elif choice == "4":
        group = input("Введіть назву групи для редагування альбомів: ")
        new_albums = input("Введіть нові альбоми (розділені комою): ").split(',')
        edit(music_library, group, new_albums)

    elif choice == "5":
        filename = input("Введіть назву файлу для збереження: ")
        save(music_library, filename)

    elif choice == "6":
        filename = input("Введіть назву файлу для завантаження: ")
        music_library = load(filename)

    elif choice == "0":
        break

    else:
        print("Невірний вибір. Будь ласка, введіть дійсну опцію.")


