from dataclasses import dataclass


@dataclass
class SearchCriteria:
    """
    Класс для описания критериев поиска книг в библиотеке.
    Позволяет задавать фильтры для поиска.
    """
    title: str | None = None
    author: str | None = None
    year: int | None = None
