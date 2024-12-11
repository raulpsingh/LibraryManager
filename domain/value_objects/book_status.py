from dataclasses import dataclass


@dataclass(frozen=True)
class BookStatus:
    """
    Класс для представления статуса книги.
    """
    value: str

    """
    Статус книги может быть, например, "В наличии" или "Выдана".
    Класс неизменяемый (frozen=True), чтобы избежать случайных изменений статуса.
    """
