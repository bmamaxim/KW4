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
        self.validate_salary()

    def __eq__(self, other):
        return int(other.__salary) == int(self.__salary)

    def __lt__(self, other):
        return int(other.__salary) < int(self.__salary)

    def validate_salary(self):
        """
        Метод валидатор, проверяет salary,
        возвращает доступное значение.
        :return: int
        """
        if self.__salary and isinstance(self.__salary, dict):
            from_ = self.__salary["from"]
            to = self.__salary["to"]
            self.__salary["from"] = from_ if from_ else 0
            self.__salary["to"] = to if to else 0
        else:
            self.__salary = {
                "from": 0,
                "to": 0,
            }

    def __str__(self):
        """
        приводим данные в читаемый вид для пользователя
        :return:
        """
        return (f"Профессия: {self.__title} \n"
                f"Ссылка: {self.__url} \n"
                f"Зарплата: {self.__salary}\n"
                f"Условия: {self.__requirements}")


    def to_dict(self):
        return {
            'title': self.__title,
            'url': self.__url,
            'salary': self.__salary,
            'requirements': self.__requirements
        }
