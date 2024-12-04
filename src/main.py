from src.functions import *
from src.library import Library
from src.messages import MESSAGES


def main():
    """
    Основная функция программы. Отвечает за взаимодействие с пользователем
    через текстовый интерфейс и выполнение соответствующих действий.
    """
    # Инициализация экземпляра класса Library для работы с книгами
    library = Library()

    # Словарь действий, связывающий номер выбора с соответствующей функцией
    actions = {
        "1": add_book,  # Добавление книги
        "2": delete_book,  # Удаление книги
        "3": search_book,  # Поиск книги
        "4": display_books,  # Отображение всех книг
        "5": change_status  # Изменение статуса книги
    }

    # Главный цикл программы
    while True:
        # Печать меню
        print(MESSAGES["menu"])

        # Получение выбора пользователя
        choice = input("\nВыберите действие: ")

        # Выполнение соответствующего действия
        if choice in actions:
            # Вызываем функцию из словаря, передавая объект библиотеки
            actions[choice](library)
        elif choice == "6":
            print(MESSAGES["exit"])
            break
        else:
            # Обработка неверного ввода
            print(MESSAGES["input_error"])


if __name__ == "__main__":
    main()
