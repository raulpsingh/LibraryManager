from dataclasses import dataclass

from domain.value_objects.book_status import BookStatus


@dataclass
class Book:
    """
    Класс, представляющий книгу в библиотеке.
    """
    book_id: int
    title: str
    author: str
    year: int
    status: BookStatus = BookStatus('В наличии')

    """
    Содержит информацию о книге: ID, название, автор, год издания и статус.
    """
