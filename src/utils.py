from src.data_vacancy.positions import Vacancy


def hh_inst(data):
    """
    Инициализируем класс HHVacancy
    :param data: json
    :return: list[dikt]
    """
    vacancy_info = []
    for info in data:
        vacancy_info.append(Vacancy(
                    title=info['professional_roles'][0]['name'],
                    url=info["alternate_url"],
                    salary=info.get['salary'],
                    requirements=info["experience"]['name']
        ))
    return vacancy_info


def sj_inst(data):
    """
    Инициализируем класс SJVacancy
    :param data: json
    :return: list[dikt]
    """
    vacancy_info = []
    for info in data:
        vacancy_info.append(Vacancy(
                    title=info['objects'][0]['profession'],
                    url=info['objects'][0]["link"],
                    salary=info.get['total'],
                    requirements=info['objects'][0]['work']
        ))
    return vacancy_info

def filter_vacancies(vacancies: list, filter_words: str) -> list[Vacancy]:
    """
    Функция фильтрации вакансий по запрошенному слову:
    filter_words. Вернет отсортированные вакансии.
    :param vacancies: list
    :param filter_words: str
    :return: list
    """
    return [vacancy
            for vacancy in vacancies
            if vacancy.title in filter_words
            ]

def sort_vacancies(filtered_vacancies: list[dict]) -> list[dict]:
    """
    Функция lambda сортирует вакансии по критерию salary
    :param filtered_vacancies: list[dict]
    :return: list[dict]
    """
    return sorted(filtered_vacancies, key=lambda vacancy: vacancy.salary, reverse=True)

def get_top_vacancies(sorted_vacancies: list[dict]) -> list[dict]:
    """
    Функция - срез первых 5 вакансий, топ 5 вакансий по ЗП.
    :param sorted_vacancies: list[dict]    :return: list[dict]
    """
    return sorted_vacancies[::5]