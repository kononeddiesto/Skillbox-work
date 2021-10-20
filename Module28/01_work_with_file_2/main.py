class File:
    """
    Контекстный менеджер для работы с файлами
    """

    def __init__(self, my_file: str, method: str) -> None:
        self.my_file, self.method = my_file, method
        self.file = None

    def __enter__(self):
        try:
            self.file = open(self.my_file, self.method, encoding='utf-8')
        except IOError:
            self.file = open(self.my_file, 'w', encoding='utf-8')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        if self.my_file:
            self.file.close()
        if exc_type is IOError:
            return True


with File('example.txt', 'a') as file:
    file.write('Всем привет!')
