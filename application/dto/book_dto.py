from dataclasses import dataclass

from domain.entities.book import Book


@dataclass
class BookDTO:
    """
    Data Transfer Object (DTO) для представления информации о книге.
    Используется для передачи данных между слоями приложения.
    """
    book_id: int
    title: str
    author: str
    year: int
    status: str

    @staticmethod
    def from_book(book: Book) -> "BookDTO":
        """
        Создаёт объект BookDTO на основе объекта Book.
        :param book: Объект Book из доменного слоя.
        :return: Экземпляр BookDTO.
        """
        return BookDTO(
            book_id=book.book_id,
            title=book.title,
            author=book.author,
            year=book.year,
            status=book.status.value
        )

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта BookDTO для удобного отображения.
        """
        return f"{self.book_id}. {self.title} - {self.author} ({self.year}) - {self.status}"
