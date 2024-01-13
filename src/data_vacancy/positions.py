class Vacancy:
    def __init__(self,
                 title: str,
                 url: str,
                 salary: str,
                 requirements: str
                 ):
        self.__title = title
        self.__url = url
        self.__salary = salary if salary else 0
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
        return f"{self.__title} {self.__url} {self.__salary} {self.__requirements}"
