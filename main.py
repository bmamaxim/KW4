
from src.data_processing.api import HeadHunterAPI, SuperJobAPI
from src.data_record.saver import JSONSaver
from src.data_vacancy.positions import Vacancy
from src.utils import hh_inst, sj_inst, filter_vacancies, sort_vacancies, get_top_vacancies




def user_interaction():
    """
    Функция для взаимодействия с пользователем
    :return: list
    """
    platforms = ["HeadHunter", "SuperJob"]
    search_query = input("Введите поисковый запрос: ")
    platform = input(f"введите платформу"
                     f"1 - {platforms[0]}"
                     f"2 - {platforms[1]}"
                     "или ENTER"
                     )
    hh_vacancies = []                                                       #список ваканситй HH
    superjob_vacancies = []                                                 #список вакансий SJ
    if platform in platforms:                                               #обрабатываем platform
        if platform == "1" or "":
            hh_api = HeadHunterAPI()
            hh_vacancies = hh_api.get_vacancies(search_query)
        elif platform == "2" or "":
            superjob_api = SuperJobAPI()
            superjob_vacancies = superjob_api.get_vacancies(search_query)
    hh_vacancies_inst = hh_inst(hh_vacancies)
    sj_vacancies_inst = sj_inst(superjob_vacancies)
    vacancies = hh_vacancies_inst + sj_vacancies_inst                       #объединяем списки HH+SJ

    filter_words = input("Введите название вакансии для фильтрации: ").split()

    filtered_vacancies = filter_vacancies(vacancies, filter_words)          #фильтруем вакансии
    if not filtered_vacancies:
        print("Нет вакансий, соответствующих заданным критериям.")
        return
    sorted_vacancies = sort_vacancies(filtered_vacancies)                   #соритруем вакансии

    top_vacancies = get_top_vacancies(sorted_vacancies)                     #топ 5 вакансий

    json_saver = JSONSaver()                                                #сохранение информации о вакансиях в файл
    json_saver.add_vacancy(sorted_vacancies)
    salary = int(input("Ведите минимальный уровень ЗП"))
    json_saver.get_vacancies_by_salary(salary)
    json_saver.delete_vacancy(top_vacancies)

    for vacancy in top_vacancies:
        print(vacancy)


if __name__ == "__main__":
    user_interaction()