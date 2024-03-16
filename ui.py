# Задача 1. Решение в группах Создать телефонный справочник возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1 Программа должна выводить данные
# 2 Программа должна сохранять данные в текстовом файле
# 3 Пользователь может ввести характеристик для поиска определенной записи(Например имя человека)
# 4 Использование функций. Ваша программа не должна быть линейной
from logger import input_data, print_data, change_data, delete_data
def interface():
    print("Добрый день! Вы попали на специальный бот спарвочник от GreekBrains! \n 1 - запись данных \n 2 - вывод данных \n 3 - изменение данных \n 4 - удаление данных")
    command = int(input())
    
    while command != 1 and command != 2 and command != 3 and command !=4:
        print("Неправильный ввод")
        command = int(input("Введите число "))

    if command == 1:
        input_data()
    elif command ==2:
        print_data()
    elif command ==3:
        change_data()
    elif command ==4:
        delete_data()