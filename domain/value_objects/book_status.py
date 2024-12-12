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
    def __post_init__(self):
        allowed_statuses = ["в наличии", "выдана"]
        if self.value.lower() not in allowed_statuses:
            raise ValueError(f"Недопустимый статус книги: {self.value}")