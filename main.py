from src.application.use_cases.add_book import AddBookUseCase
from src.application.use_cases.change_status import ChangeBookStatusUseCase
from src.application.use_cases.remove_book import RemoveBookUseCase
from src.application.use_cases.search_book import SearchBookUseCase
from src.infrastructure.repositories.json_library_repository import JsonLibraryRepository
from src.presentation.cli.menu import display_menu, add_book, delete_book, search_books, display_books, change_status


def main():
    # Создание экземпляра репозитория с указанием пути к файлу базы данных
    repo = JsonLibraryRepository("src/infrastructure/database/books.json")

    # Инициализация сценариев использования, передача репозитория в качестве зависимости
    add_book_use_case = AddBookUseCase(repo)
    change_status_use_case = ChangeBookStatusUseCase(repo)
    delete_book_use_case = RemoveBookUseCase(repo)
    search_book_use_case = SearchBookUseCase(repo)

    # Определение словаря действий, где ключи - это выбор пользователя, а значения - функции, которые нужно выполнить
    actions = {
        "1": lambda: add_book(add_book_use_case),  # Добавление книги
        "2": lambda: delete_book(delete_book_use_case),  # Удаление книги
        "3": lambda: search_books(search_book_use_case),  # Поиск книги
        "4": lambda: display_books(repo.books),  # Отображение всех книг
        "5": lambda: change_status(change_status_use_case),  # Изменение статуса книги
    }

    # Запуск главного меню и обработка пользовательского ввода
    display_menu(actions)


# Точка входа в приложение
if __name__ == "__main__":
    main()
