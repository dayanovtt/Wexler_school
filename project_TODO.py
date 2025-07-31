import os
import json

def print_with_indent(value, indent=0):
    indentation = '\t' * indent
    print(f'{indentation}{value}')


class Entry:

    def __init__(self, title, entries=None, parent=None):
        if entries is None:
            entries = []
        self.title = title
        self.entries = entries
        self.parent = parent

    def print_entries(self, indent=0):
        print_with_indent(self, indent)
        for grocery in self.entries:
            grocery.print_entries(indent + 1)

    def json(self):
        entry_titles = [entry.json() for entry in self.entries]
        dict_sample = {'title': self.title, 'entries': entry_titles}
        return dict_sample

    @classmethod
    def from_json(cls, value):
        new_entry = cls(value['title'])
        for sub_entry in value.get('entries', []):
            new_entry.add_entry(cls.from_json(sub_entry))
        return new_entry

    def add_entry(self, new_value):
        self.entries.append(new_value)
        new_value.parent = self

    def save(self, path):
        value1 = self.json()
        with open(path, 'w') as self.title:
            value2 = json.dumps(value1)
            self.title.write(value2)

entry = {"title": "Дела по дому", "entries": []}
category = Entry.from_json(entry)