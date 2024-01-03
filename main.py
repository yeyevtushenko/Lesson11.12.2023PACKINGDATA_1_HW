import json
import gzip

def add(library, group, albums):
    if group not in library:
        library[group] = albums
    else:
        print(f"Група  {group} вже є у бібліотеці.")
