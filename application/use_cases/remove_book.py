from application.interfaces.library_repository import LibraryRepository


class RemoveBookUseCase:
    """
    Класс для удаления книги из библиотеки.
    """

    def __init__(self, repository: LibraryRepository) -> None:
        """
        Инициализация класса.
        :param repository: Экземпляр репозитория для работы с данными библиотеки.
        """
        self.repository = repository

    def execute(self, book_id: int) -> None:
        """
        Удаляет книгу из библиотеки по её идентификатору.
        :param book_id: Идентификатор книги.
        :raises ValueError: Если книга с указанным идентификатором не найдена.
        """
        if not self.repository.remove_book_from_library(book_id=book_id):
            raise ValueError("Книга не найдена")
