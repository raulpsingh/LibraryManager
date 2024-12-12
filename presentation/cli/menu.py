from application.dto.book_dto import BookDTO
from application.dto.search_criteria import SearchCriteria
from presentation.cli.messages import MESSAGES


def display_menu(actions) -> None:
    """
    Отображает главное меню и обрабатывает выбор пользователя.
    :param actions: Словарь, где ключи - действия, значения - функции.
    """
    while True:
        print(MESSAGES["menu"])
        choice = input("\nВыберите действие: ")

        if choice in actions:
            actions[choice]()
        elif choice == "6":
            print(MESSAGES["exit"])
            break
        else:
            print(MESSAGES["input_error"])


def validate_input_is_correct_id(book_id: str) -> int:
    """
    Проверяет, что введённое значение является числом.
    :param book_id: Входная строка для проверки.
    :return: True, если строка состоит из цифр, иначе False.
    """

    if not book_id.isdigit():
        raise ValueError(MESSAGES["status_id_error"])
    return int(book_id)


def validate_year(year: str) -> int:
    """
    Проверяет, что введённое значение является корректным годом.
    :param year: Входная строка для проверки.
    :return: Int год.
    """
    if not year.isdigit():
        raise ValueError(MESSAGES["add_year_error"])
    year = int(year)
    if not (868 <= year <= 2024):
        raise ValueError(MESSAGES["year_error"])

    return year


def validate_status(status: str) -> str:
    """
    Проверяет, что введённое значение является корректным статусом.
    :param status: Входная строка для проверки.
    :return: Str статус.
     """
    if status.lower() not in ["в наличии", "выдана"]:
        raise ValueError(MESSAGES["status_invalid"])
    return status.title()


def get_book_details() -> tuple[str, str, int]:
    """
    Получает данные о книге от пользователя.
    :return: Кортеж с названием, автором и годом выпуска книги.
    """
    title = input(MESSAGES["add_prompt_title"])
    author = input(MESSAGES["add_prompt_author"])
    year = validate_year(input(MESSAGES["add_prompt_year"]))
    return title, author, year


def get_book_id() -> int:
    """
    Получает ID книги от пользователя.
    :return: ID книги.
    """
    book_id = validate_input_is_correct_id(input(MESSAGES["prompt_id"]))
    return book_id


def get_book_status() -> str:
    """
    Получает новый статус книги от пользователя.
    :return: Новый статус книги.
    """
    status = validate_status(input(MESSAGES["status_prompt_new"]))
    return status


def add_book(use_case) -> None:
    """
    Добавляет книгу с помощью переданного use case.
    :param use_case: Объект для выполнения бизнес-логики добавления книги.
    """
    try:
        title, author, year = get_book_details()
        use_case.execute(title, author, year)
        print(MESSAGES["add_success"])
    except ValueError as e:
        print(e)


def delete_book(use_case) -> None:
    """
    Удаляет книгу с помощью переданного use case.
    :param use_case: Объект для выполнения бизнес-логики удаления книги.
    """
    try:
        book_id = get_book_id()
        use_case.execute(book_id)
        print(MESSAGES["delete_success"])
    except ValueError as e:
        print(e)


def search_books(use_case) -> None:
    """
    Выполняет поиск книг по критериям.
    :param use_case: Объект для выполнения бизнес-логики поиска книг.
    """
    query = input(MESSAGES["search_prompt"])
    criteria = SearchCriteria(title=query, author=query, year=int(query) if query.isdigit() else None)  # type: ignore
    results = use_case.execute(criteria)
    if results:
        for book in results:
            print(book)
    else:
        print(MESSAGES["search_not_found"])


def display_books(books) -> None:
    """
    Отображает список книг.
    :param books: Список объектов книг.
    """
    if books:
        for book in books:
            print(BookDTO.from_book(book))
    else:
        print(MESSAGES["no_books"])


def change_status(use_case) -> None:
    """
    Изменяет статус книги с помощью переданного use case.
    :param use_case: Объект для выполнения бизнес-логики изменения статуса.
    """
    try:
        book_id = get_book_id()
        new_status = get_book_status()
        use_case.execute(book_id, new_status)
        print(MESSAGES["status_success"])
    except ValueError as e:
        print(e)
