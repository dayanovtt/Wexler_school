class File:
    def __init__(self, path, filename, extension='png'):
        self.path = path
        self.filename = filename
        self.extension = extension
        self.is_opened = False

    def __str__(self):
        return f'{self.path}/{self.filename}.{self.extension}'

    def open(self):
        if self.is_opened == False:
            self.is_opened = True
        else:
            return f'Ошибка. Файл {str(self)} уже открыт'

    def close(self):
        if self.is_opened == True:
            self.is_opened = False
        else:
            return f'Ошибка. Файл {str(self)} уже закрыт'

    def read(self):
        if self.is_opened == True:
            return self.filename
        else:
            return f'Ошибка чтения. Файл {str(self)} закрыт'


class VideoFile(File):

    def __init__(self, path, filename, length='0:00', extension='png'):
        super().__init__(path, filename, extension)

        self.length = length


video_file = VideoFile('top_movies', 'Mimino', 'mkv', '97:00')
file1 = File('c:/', 'name1')
file2 = File('d:/', 'name2', 'jpeg')

print(file1)
print(file2)

file1.open()
