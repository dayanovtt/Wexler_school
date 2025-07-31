def write_to_file(filename, content):
    value = (f'{filename} {content}')
    with open('my_file.txt', 'w') as file:
        file.write(value)


write_to_file('/users/egor/hello_world.txt', 'Hello World')
