from src.application.interfaces.library_repository import LibraryRepository
from src.domain.value_objects.book_status import BookStatus


class ChangeBookStatusUseCase:
    """
    Класс для изменения статуса книги в библиотеке.
    """

    def __init__(self, repository: LibraryRepository) -> None:
        """
        Инициализация класса.
        :param repository: Экземпляр репозитория для работы с данными библиотеки.
        """
        self._repository = repository

    def execute(self, book_id: int, new_status: str) -> None:
        """
        Изменяет статус книги по её идентификатору.
        :param book_id: Идентификатор книги.
        :param new_status: Новый статус книги (например, "В наличии" или "Выдана").
        :raises ValueError: Если книга с указанным идентификатором не найдена.
        """
        # Преобразуем строковое значение статуса в объект BookStatus
        status = BookStatus(new_status)
        if not self._repository.change_book_status(book_id, status):
            raise ValueError("Книга не найдена")
