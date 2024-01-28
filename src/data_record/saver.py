import json
from abc import ABC, abstractmethod


from config import JSON_PATH


class Saver(ABC):
    """
    Класс с методами записи, читения, сохранения
    json данных по вакансиям, переданны из "main"
    """
    @abstractmethod
    def add_vacancy(self, vacancies: list) -> None:
        """
        Метод записи в файл, по заданному пути: "JSON_PATH",
        данных по вакансиям переданных из "main"
        :param vacancies: list
        :return: None
        """
        raise NotImplemented

    @abstractmethod
    def get_vacancies_by_salary(self, salary: str) -> list[dict]:
        """
        Метод принимает запрос пользователя по фильтрации вакансий.
        Читает файл с данными записанными add_vacancy
        Фильтрует вакансии по критерию salary
        :param salary: str
        :return: list
        """
        raise NotImplemented

    @abstractmethod
    def delete_vacancy(self, vacancy: dict) -> None:
        """
        Перезаписывает файл с вакансиями по условию:
        в методе get_vacancies_by_salary
        """
        raise NotImplemented

class JSONSaver(Saver):

    def add_vacancy(self, vacancies: list) -> None:
        vacancy = [vacansy.to_dict() for vacansy in vacancies]
        with open(JSON_PATH, 'w', encoding='utf-8') as file:
            json.dump(vacancy, file)

    def get_vacancies_by_salary(self, salary: int) -> list[dict]:
        vacancies = reading_file()
        vacancies_by_salary = []
        if salary:
            for vacancy in vacancies:
              pass
                #return vacancies_by_salary
        #return vacancies

    def delete_vacancy(self, vacancy: dict) -> None:
        with open(JSON_PATH, 'w', encoding='utf-8') as file:
            json.dump(vacancy, file)


def reading_file():
    with open(JSON_PATH, 'r', encoding='utf-8') as file:
        return json.load(file)

def record_vacancy(vacancies: list) -> None:
    with open(JSON_PATH, 'w', encoding='utf-8') as file:
        json.dump(vacancies, file)
