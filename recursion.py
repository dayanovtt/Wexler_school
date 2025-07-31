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

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

    def add_entry(self, new_value):
        self.entries.append(new_value)
        new_value.parent = self

    def print_entries(self, indent=0):
        print_with_indent(self, indent)
        for grocery in self.entries:
            grocery.print_entries(indent + 1)

    def json(self):
        entry_titles = [entry.title for entry in self.entries]
        dict_sample = {'title': self.title, 'entries': entry_titles}
        return dict_sample

groceries = Entry('Продукты')
category = Entry('Мясное')

groceries.add_entry(Entry('Молоко'))
category.add_entry(Entry('Курица'))
category.add_entry(Entry('Говядина'))
category.add_entry(Entry('Колбаса'))

groceries.add_entry(category)

groceries.print_entries()
category = Entry('Еда')

category.add_entry(Entry('Морковь'))
category.add_entry(Entry('Капуста'))

category.json()