from infrastructure.repositories.json_library_repository import JsonLibraryRepository
from application.use_cases.add_book import AddBookUseCase
from application.use_cases.change_status import ChangeBookStatusUseCase
from application.use_cases.remove_book import RemoveBookUseCase
from application.use_cases.search_book import SearchBookUseCase
from presentation.cli.menu import display_menu, add_book, delete_book, search_books, display_books, change_status


def main():
    repo = JsonLibraryRepository("infrastructure/database/books.json")
    add_book_use_case = AddBookUseCase(repo)
    change_status_use_case = ChangeBookStatusUseCase(repo)
    delete_book_use_case = RemoveBookUseCase(repo)
    search_book_use_case = SearchBookUseCase(repo)

    actions = {
        "1": lambda: add_book(add_book_use_case),
        "2": lambda: delete_book(delete_book_use_case),
        "3": lambda: search_books(search_book_use_case),
        "4": lambda: display_books(repo.books),
        "5": lambda: change_status(change_status_use_case),
    }

    display_menu(actions)


if __name__ == "__main__":
    main()
