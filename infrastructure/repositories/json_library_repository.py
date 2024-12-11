import json

from application.dto.search_criteria import SearchCriteria
from application.interfaces.library_repository import LibraryRepository
from domain.entities.book import Book
from domain.value_objects.book_status import BookStatus


class JsonLibraryRepository(LibraryRepository):
    """
    Реализация интерфейса LibraryRepository для работы с хранилищем книг в формате JSON.
    Обеспечивает методы для добавления, удаления, поиска и изменения статуса книг.
    """

    def __init__(self, data_file: str) -> None:
        """
        Инициализация репозитория.
        :param data_file: Путь к JSON-файлу с данными о книгах.
        """
        self.data_file = data_file
        self.books = self._load_books()

    def _load_books(self) -> list[Book]:
        """
        Загружает книги из JSON-файла в память.
        :return: Список объектов Book.
        """
        try:
            with open(self.data_file, 'r', encoding='utf-8') as file:
                return [
                    Book(
                        book_id=book['book_id'],
                        title=book['title'],
                        author=book['author'],
                        year=book['year'],
                        status=BookStatus(book['status'])
                    ) for book in json.load(file)
                ]
        except FileNotFoundError:
            # Если файл отсутствует, создаём его и возвращаем пустой список
            with open(self.data_file, 'w', encoding='utf-8') as file:
                json.dump([], file)
            return []

    def _save_books(self) -> None:
        """
        Сохраняет текущий список книг в JSON-файл.
        """
        with open(self.data_file, 'w', encoding='utf-8') as file:
            json.dump([
                {
                    'book_id': book.book_id,
                    'title': book.title,
                    'author': book.author,
                    'year': book.year,
                    'status': book.status.value
                } for book in self.books
            ], file, ensure_ascii=False, indent=4)

    def add_book_to_library(self, book: Book) -> None:
        """
        Добавляет книгу в хранилище и сохраняет изменения в файл.
        :param book: Объект Book для добавления.
        """
        self.books.append(book)
        self._save_books()

    def remove_book_from_library(self, book_id: int) -> bool:
        """
        Удаляет книгу из хранилища по её ID.
        :param book_id: Идентификатор книги.
        :return: True, если книга была удалена, иначе False.
        """
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                self._save_books()
                return True
        return False

    def search_book_in_library(self, criteria: SearchCriteria) -> list[Book] | None:
        """
        Ищет книги в хранилище по заданным критериям.
        :param criteria: Объект SearchCriteria с параметрами поиска.
        :return: Список найденных книг или None, если ничего не найдено.
        """
        result = [
            book for book in self.books
            if (criteria.title and criteria.title.lower() in book.title.lower()) or
               (criteria.author and criteria.author.lower() in book.author.lower()) or
               (criteria.year and criteria.year == book.year)
        ]
        return result if result else None

    def change_book_status(self, book_id: int, new_status: BookStatus) -> bool:
        """
        Изменяет статус книги по её ID.
        :param book_id: Идентификатор книги.
        :param new_status: Новый статус книги.
        :return: True, если статус был успешно изменён, иначе False.
        """
        for book in self.books:
            if book.book_id == book_id:
                book.status = new_status
                self._save_books()
                return True
        return False
