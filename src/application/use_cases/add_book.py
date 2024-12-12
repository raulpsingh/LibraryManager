from src.application.interfaces.library_repository import LibraryRepository
from src.domain.entities.book import Book


class AddBookUseCase:
    """
    Класс для добавления книги в библиотеку с использованием репозитория.
    """

    def __init__(self, repository: LibraryRepository) -> None:
        """
        Инициализация класса.
        :param repository: Экземпляр репозитория для работы с данными библиотеки.
        """
        self.repository = repository

    def execute(self, title: str, author: str, year: int) -> None:
        """
        Добавляет новую книгу в библиотеку.
        :param title: Название книги.
        :param author: Автор книги.
        :param year: Год издания книги.
        """
        # Определяем ID для новой книги, основываясь на текущих данных репозитория
        book_id = max((book.book_id for book in self.repository.books), default=0) + 1  # type: ignore
        book = Book(book_id=book_id, title=title, author=author, year=year)
        self.repository.add_book_to_library(book)
