import os
from abc import ABC, abstractmethod

import requests

from config import HHru_URL, SJ_URL


class API(ABC):
    """
    Абстрактный API класс c методом запроса
    """
    @abstractmethod
    def get_vacancies(self, query) -> list[dict]:
        raise NotImplementedError


class HeadHunterAPI(API):
    """
    API класс ресурса поиска работы HeadHunter
    """

    def get_vacancies(self, query) -> list[dict]:
        """
        Метод запроса данных с HeadHunter по параметрам
        с проверкой на доступность данных.
        :return: json
        """
        params = {'resp': query}
        response = requests.get(HHru_URL, params=params)
        if response.status_code != 200:
            raise RecursionError(f'{response.status_code}')
        else:
            return response.json()

class SuperJobAPI(API):
    """
    API класс ресурса поиска работы SuperJob
    """
    headers = {
        'X - Api - App - Id': os.getenv('v3.r.138066651.1f4e09038afc30ca610ec3a2db67392bf76dc3f5.72751091098d054ea6330d27e6ae7b45f53ef2a5')
                }

    def get_vacancies(self, query) -> list[dict]:
        """
        Метод запроса данных с SuperJob по параметрам
        с проверкой на доступность данных.
        :return: json
        """
        params = {'word': query}
        response = requests.get(SJ_URL, params=params, headers=self.headers)
        if response.status_code != 200:
            return response.json()
        if response.status_code == 500:
            raise RecursionError(f'{response.status_code}')
