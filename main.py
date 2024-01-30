from src.data_processing.api import HeadHunterAPI, SuperJobAPI
from src.data_record.saver import JSONSaver, reading_file
from src.utils import hh_inst, sj_inst, sort_vacancies, get_top_vacancies, filter_vacancies, gen_cont


def user_interaction():
    """
    Функция для взаимодействия с пользователем
    :return: list
    """
    platforms = ["HeadHunter", "SuperJob"]                                                  # выбор платформы
    search_query: str = input("Введите поисковый запрос: \n")
    platform = input(f"введите платформу\n"
                     f"1 - {platforms[0]}\n"
                     f"2 - {platforms[1]}\n"
                     )

    hh_vacancies = []                                                                       # список ваканситй HH
    superjob_vacancies = []                                                                 # список вакансий SJ
    if platform == "1":
        hh_api = HeadHunterAPI()
        hh_vacancies.append(hh_api.get_vacancies(search_query))
    elif platform == "2":
        superjob_api = SuperJobAPI()
        superjob_vacancies.append(superjob_api.get_vacancies(search_query))
    else:
        superjob_api = SuperJobAPI()
        hh_api = HeadHunterAPI()
        superjob_vacancies.append(superjob_api.get_vacancies(search_query))
        hh_vacancies.append(hh_api.get_vacancies(search_query))

    hh_vacancies_inst = hh_inst(hh_vacancies)                                                # инициализированный список HH
    sj_vacancies_inst = sj_inst(superjob_vacancies)                                          # # инициализированный список SJ
    vacancies = [hh_vacancies_inst, sj_vacancies_inst]                                       # объединение списков

    json_saver = JSONSaver()                                                                 # сохранение информации о вакансиях в файл
    json_saver.add_vacancy(vacancies[1])

    filter_words = input("Введите название вакансии для фильтрации: \n").split()             # фильтруем вакансии
    filtered_vacancies = filter_vacancies(reading_file(), filter_words)

    if not filtered_vacancies:
        print("Нет вакансий, соответствующих заданным критериям.")
        return

    sorted_vacancies = sort_vacancies(filtered_vacancies)                                        # соритруем вакансии
    top_vacancies = get_top_vacancies(sorted_vacancies)                                      # топ вакансий
    json_saver.delete_vacancy(top_vacancies)                                                 # удаление вакансий
    for vacancy in top_vacancies:                                                            # вывод информации в терминал
        print(f""" \n 
    {vacancy['title']}
    Ссылка: {vacancy['url']}
    Зарплата: {vacancy['salary']['from']} - {vacancy['salary']['to']}\n
    """)

    #salary = input("Введите минимальный уровень ЗП\n")
    #json_saver.get_vacancies_by_salary(salary)

    #filtered_vacancies = filter_vacancies(vacancies, filter_words)


if __name__ == "__main__":
    user_interaction()
