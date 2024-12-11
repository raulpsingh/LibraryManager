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


def validate_input_is_numeric(input_to_validate: str) -> bool:
    """
    Проверяет, что введённое значение является числом.
    :param input_to_validate: Входная строка для проверки.
    :return: True, если строка состоит из цифр, иначе False.
    """
    return input_to_validate.isnumeric()


def get_book_details() -> tuple[str, str, int]:
    """
    Получает данные о книге от пользователя.
    :return: Кортеж с названием, автором и годом выпуска книги.
    """
    title = input(MESSAGES["add_prompt_title"])
    author = input(MESSAGES["add_prompt_author"])
    year = input(MESSAGES["add_prompt_year"])
    if validate_input_is_numeric(year):
        return title, author, int(year)
    raise ValueError(MESSAGES['input_error'])


def get_book_id() -> int:
    """
    Получает ID книги от пользователя.
    :return: ID книги.
    """
    book_id = input(MESSAGES["prompt_id"])
    if validate_input_is_numeric(book_id):
        return int(book_id)
    raise ValueError(MESSAGES['input_error'])


def get_book_status() -> str:
    """
    Получает новый статус книги от пользователя.
    :return: Новый статус книги.
    """
    status = input(MESSAGES["status_prompt_new"])
    if status.lower() in ["выдана", "в наличии"]:
        return status
    raise ValueError(MESSAGES['input_error'])


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
