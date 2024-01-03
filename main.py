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
