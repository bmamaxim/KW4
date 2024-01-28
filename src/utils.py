from src.data_record.saver import reading_file
from src.data_vacancy.positions import Vacancy


def hh_inst(data):
    """
    Инициализируем класс HHVacancy
    :param data: json
    :return: list[dikt]
    """
    vacancy_info = []
    if data:
        for info in data[0]['items']:
            vacancy_info.append(Vacancy(
                        title=info['name'],
                        url=info["alternate_url"],
                        salary=info.get('salary'),
                        requirements=info['experience']['name']
            ))
        return vacancy_info


def sj_inst(data):
    """
    Инициализируем класс SJVacancy
    :param data: json
    :return: list[dikt]
    """
    vacancy_info = []
    if data:
        for info in data[0]['objects']:
            vacancy_info.append(Vacancy(
                        title=info['profession'],
                        url=info["link"],
                        salary={"from": info['payment_from'], "to": info['payment_to']},
                        requirements=info['work']
            ))
        return vacancy_info

def filter_vacancies(vacancies: list, filter_words: str):
    """
    Функция фильтрации вакансий по запрошенному слову:
    filter_words. Вернет отсортированные вакансии.
    :param vacancies: list
    :param filter_words: str
    :return: list
    """
    if filter_words:
        filtered_vacancies = []
        for vacansy in vacancies:
            for word in filter_words:
                if word in vacansy['title']:
                    return filtered_vacancies.append(vacansy)
    return vacancies

def sort_vacancies(filtered_vacancies: list[dict]) -> list[dict]:
    """
    Функция lambda сортирует вакансии по критерию salary
    :param filtered_vacancies: list[dict]
    :return: list[dict]
    """
    return sorted(filtered_vacancies, key=lambda vacancy: (vacancy['salary']["from"] + vacancy['salary']["to"]) / 2, reverse=True)

def get_top_vacancies(sorted_vacancies: list[dict]) -> list[dict]:
    """
    Функция - срез первых 5 вакансий, топ 5 вакансий по ЗП.
    :param sorted_vacancies: list[dict]    :return: list[dict]
    """
    return sorted_vacancies[::5]
