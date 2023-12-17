# Клас, який реалізує патерн Одинак
class FileManager:
    # Приватне поле для збереження єдиного екземпляра класу
    instance = None

    # Приватний конструктор, щоб заборонити створення екземплярів класу ззовні
    def __init__(self):
        # Ініціалізація даних та налаштувань
        pass

    # Метод для отримання єдиного екземпляра класу
    @classmethod
    def getInstance(cls):
        # Перевірка, чи існує вже екземпляр класу
        if cls.instance is None:
            # Якщо екземпляр не існує, то створюємо його
            cls.instance = cls()
        return cls.instance

    # Метод для зміни сховища користувача
    def setStorage(self, storageType):
        # Логіка для зміни сховища
        pass

    # Метод для завантаження файлу
    def uploadFile(self, fileName, content):
        # Логіка для завантаження файлу
        pass

    # Метод для завантаження файлу
    def downloadFile(self, fileName):
        # Логіка для завантаження файлу
        pass


# Головний код
def main():
    # Отримуємо єдиний екземпляр класу FileManager
    fileManager = FileManager.getInstance()

    # Встановлюємо сховище для користувача
    fileManager.setStorage("Amazon S3")

    # Завантажуємо файл
    fileManager.uploadFile("example.txt", "Це вміст файлу.")

    # Завантажуємо файл
    fileContent = fileManager.downloadFile("example.txt")

    # Виводимо вміст завантаженого файлу
    print("Завантажений файл:", fileContent)


# Виклик головного коду
if __name__ == "__main__":
    main()