from src.application.dto.book_dto import BookDTO
from src.application.dto.search_criteria import SearchCriteria
from src.application.interfaces.library_repository import LibraryRepository


class SearchBookUseCase:
    """
    Класс для поиска книг в библиотеке по заданным критериям.
    """

    def __init__(self, repository: LibraryRepository) -> None:
        """
        Инициализация класса.
        :param repository: Экземпляр репозитория для работы с данными библиотеки.
        """
        self.repository = repository

    def execute(self, criteria: SearchCriteria) -> list[BookDTO] | None:
        """
        Выполняет поиск книг в библиотеке.
        :param criteria: Критерии поиска (название, автор, год).
        :return: Список найденных книг в формате DTO или None, если ничего не найдено.
        """
        books = self.repository.search_book_in_library(criteria)
        return [BookDTO.from_book(book) for book in books] if books else None
