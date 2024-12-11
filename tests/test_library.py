import unittest

from application.dto.search_criteria import SearchCriteria
from application.interfaces.library_repository import LibraryRepository
from application.use_cases.add_book import AddBookUseCase
from application.use_cases.change_status import ChangeBookStatusUseCase
from application.use_cases.remove_book import RemoveBookUseCase
from application.use_cases.search_book import SearchBookUseCase
from domain.entities.book import Book
from domain.value_objects.book_status import BookStatus


class MockLibraryRepository(LibraryRepository):
    def __init__(self):
        self.books = []

    def add_book_to_library(self, book: Book) -> None:
        self.books.append(book)

    def remove_book_from_library(self, book_id: int) -> bool:
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                return True
        return False

    def search_book_in_library(self, criteria: SearchCriteria) -> list[Book] | None:
        result = [
            book for book in self.books
            if (criteria.title and criteria.title.lower() in book.title.lower()) or
               (criteria.author and criteria.author.lower() in book.author.lower()) or
               (criteria.year and criteria.year == book.year)
        ]
        return result if result else None

    def change_book_status(self, book_id: int, new_status: BookStatus) -> bool:
        for book in self.books:
            if book.book_id == book_id:
                book.status = new_status
                return True
        return False


class TestLibraryMethods(unittest.TestCase):
    """
    Тесты для методов библиотеки с использованием Mock репозитория.
    """

    def setUp(self):
        """
        Метод setup, который выполняется перед каждым тестом.
        Создаём тестовую библиотеку с несколькими книгами.
        """
        self.repository = MockLibraryRepository()
        self.repository.books = [
            Book(book_id=1, title="Изучаем Python", author="Эрик Мэтиз", year=2024, status=BookStatus("В наличии")),
            Book(book_id=2, title="Грокаем Алгоритмы", author="Адитья Бхаргава", year=2017, status=BookStatus("Выдана"))
        ]
        self.add_book_use_case = AddBookUseCase(self.repository)
        self.remove_book_use_case = RemoveBookUseCase(self.repository)
        self.search_book_use_case = SearchBookUseCase(self.repository)
        self.change_status_use_case = ChangeBookStatusUseCase(self.repository)

    def test_add_book(self):
        """Тест добавления книги."""
        self.add_book_use_case.execute("A Byte of Python", "Swaroop Chitlur", 2013)
        self.assertEqual(len(self.repository.books), 3)
        self.assertEqual(self.repository.books[2].title, "A Byte of Python")
        self.assertEqual(self.repository.books[2].author, "Swaroop Chitlur")

    def test_delete_book(self):
        """Тест удаления книги по ID."""
        self.remove_book_use_case.execute(1)
        self.assertEqual(len(self.repository.books), 1)
        self.assertEqual(self.repository.books[0].title, "Грокаем Алгоритмы")

    def test_delete_non_existent_book(self):
        """Тест попытки удаления несуществующей книги."""
        with self.assertRaises(ValueError):
            self.remove_book_use_case.execute(999)

    def test_search_book_by_title(self):
        """Тест поиска книги по названию."""
        criteria = SearchCriteria(title="Изучаем Python")
        result = self.search_book_use_case.execute(criteria)
        self.assertIsNotNone(result)
        self.assertEqual(result[0].title, "Изучаем Python")

    def test_search_book_by_author(self):
        """Тест поиска книги по автору."""
        criteria = SearchCriteria(author="Адитья Бхаргава")
        result = self.search_book_use_case.execute(criteria)
        self.assertIsNotNone(result)
        self.assertEqual(result[0].author, "Адитья Бхаргава")

    def test_search_book_by_year(self):
        """Тест поиска книги по году."""
        criteria = SearchCriteria(year=2024)
        result = self.search_book_use_case.execute(criteria)
        self.assertIsNotNone(result)
        self.assertEqual(result[0].year, 2024)

    def test_change_status(self):
        """Тест изменения статуса книги."""
        self.change_status_use_case.execute(2, "В наличии")
        self.assertEqual(self.repository.books[1].status.value, "В наличии")

    def test_change_status_invalid_id(self):
        """Тест изменения статуса книги с несуществующим ID."""
        with self.assertRaises(ValueError):
            self.change_status_use_case.execute(999, "Выдана")


if __name__ == "__main__":
    unittest.main()
