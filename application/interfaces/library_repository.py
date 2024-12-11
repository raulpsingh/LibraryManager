from abc import ABC, abstractmethod

from application.dto.search_criteria import SearchCriteria
from domain.entities.book import Book
from domain.value_objects.book_status import BookStatus


class LibraryRepository(ABC):
    """
    Абстрактный класс, определяющий интерфейс для работы с репозиторием библиотеки.
    Этот интерфейс должен быть реализован в конкретных репозиториях (например, JSON, БД и т.д.).
    """

    @abstractmethod
    def add_book_to_library(self, book: Book) -> None:
        """
        Добавляет книгу в репозиторий.
        :param book: Объект книги для добавления.
        """
        pass

    @abstractmethod
    def remove_book_from_library(self, book_id: int) -> bool:
        """
        Удаляет книгу из репозитория по её ID.
        :param book_id: Идентификатор книги.
        :return: True, если книга успешно удалена, иначе False.
        """
        pass

    @abstractmethod
    def search_book_in_library(self, criteria: SearchCriteria) -> list[Book] | None:
        """
        Ищет книги в репозитории по заданным критериям.
        :param criteria: Критерии поиска (название, автор, год).
        :return: Список найденных книг или None, если книги не найдены.
        """
        pass

    @abstractmethod
    def change_book_status(self, book_id: int, new_status: BookStatus) -> bool:
        """
        Изменяет статус книги в репозитории.
        :param book_id: Идентификатор книги.
        :param new_status: Новый статус книги.
        :return: True, если статус успешно изменён, иначе False.
        """
        pass
