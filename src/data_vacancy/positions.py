class Vacancy:
    def __init__(self,
                 title: str,
                 url: str,
                 salary: str,
                 requirements: str
                 ) -> object:
        self.__title = title
        self.__url = url
        self.__salary = salary
        self.__requirements = requirements

    def __gt__(self, other):
        return other.__salary > self.__salary

    def __lt__(self, other):
        return other.__salary < self.__salary

    def __str__(self):
        """
        приводим данные в читаемый вид для пользователя
        :return:
        """
        return (f"Профессия {self.__title} \n"
                f"Ссылка {self.__url} \n"
                f"Зарплата {self.__salary} \n"
                f"Условия {self.__requirements}")

    def validate_salary(self):
        """
        Метод валидатор, проверяем в какой валютеописана зарплата,
        возвращает доступную.
        :return: int
        """
        if self.__salary and isinstance(self.__salary, dict):
            from_ = self.__salary.get("from")
            to = self.__salary.get("to")
            self.__salary["from"] = from_ if from_ else 0
            self.__salary["to"] = to if to else 0
        else:
            self.__salary = {
                "from": 0,
                "to": 0,
            }

    def to_dict(self):
        return {
            'title': self.__title,
            'url': self.__url,
            'salary': self.__salary,
            'requirements': self.__requirements
        }

class HHVacancy(Vacancy):
    def __str__(self):
        return (f"Профессия на hh.ru {self.__title} \n"
                f"Ссылка {self.__url} \n"
                f"Зарплата {self.__salary} \n"
                f"Условия {self.__requirements}")

class SJVacancy(Vacancy):
    def __str__(self):
        return (f"Профессия на sj {self.__title} \n"
                f"Ссылка {self.__url} \n"
                f"Зарплата {self.__salary} \n"
                f"Условия {self.__requirements}")
