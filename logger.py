from data_cteate import name_data, surname_data, phone_data, address_data

def input_data():
    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:         
        lines = f.readlines()     
        m = len(lines) # Рассчитываем номер записи 
    with open('data_second_variant.csv', 'r', encoding='utf-8') as f:         
        lines1 = f.readlines()     
        v = len(lines1)  # Рассчитываем номер записи 
    name = name_data()
    surname= surname_data()
    phone = phone_data()
    address= address_data()
    var = int(input(f"В каком формате записать данные \n\n"
    f"1 Вариант:\n"
    f"{name}\n{surname}\n{phone}\n{address}\n\n"
    f"2 Вариант:\n"
    f"{name};{surname};{phone};{address}\n"
    f"Выберите вариант: "))
    
    while var != 1 and var != 2:
        print("Неправильный ввод")
        var = int(input("Введите число "))
    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address} \n\n")
    elif var == 2:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name};{surname};{phone};{address}\n\n") 

def print_data():
    print("Вывожу данные из 1-ого файла: \n")
    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] =='\n' or i == len(data_first) - 1:
                data_first_list.append(''.join(data_first[j:i + 1]))
                j = i
        data_first_list_final = []

        for i in range(len(data_first_list)):  # Удаляем дублирующиеся переносы строк в списке
            if data_first_list[i] != '\n\n':
                data_first_list_final.append(data_first_list[i])
        print(''.join(data_first_list_final))

    print("Вывожу данные из 2-ого файла: \n")
    with open('data_second_variant.csv','r', encoding='utf-8') as f:
        data_second = f.readlines()
        print(*data_second)       

def change_data():
    file_choice = int(input("Выберите файл для внесения изменений (1 - data_first_variant.csv, 2 - data_second_variant.csv): "))
    field_choice = int(input("Выберите поле для изменения (1 - имя, 2 - фамилия, 3 - телефон, 4 - адрес): "))
    
    if file_choice == 1:
        with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
            old_data = f.readlines()
        filename = 'data_first_variant.csv'
    elif file_choice == 2:
        with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
            old_data = f.readlines()
        filename = 'data_second_variant.csv'
    
    print("Старые данные:")
    print(*old_data, sep='')
    
    record_number = int(input("Введите номер записи для изменения: "))
    
    if field_choice == 1:
        new_name = input("Введите новое имя: ")
        old_field = old_data[(record_number-1)*4].strip()
        old_data[(record_number-1)*4] = new_name + '\n'
    elif field_choice == 2:
        new_surname = input("Введите новую фамилию: ")
        old_field = old_data[(record_number-1)*4 + 1].strip()
        old_data[(record_number-1)*4 + 1] = new_surname + '\n'
    elif field_choice == 3:
        new_phone = input("Введите новый телефон: ")
        old_field = old_data[(record_number-1)*4 + 2].strip()
        old_data[(record_number-1)*4 + 2] = new_phone + '\n'
    elif field_choice == 4:
        new_address = input("Введите новый адрес: ")
        old_field = old_data[(record_number-1)*4 + 3].strip()
        old_data[(record_number-1)*4 + 3] = new_address + '\n\n'
    
    print(f"Старое значение: {old_field}")
    print("Новые данные:")
    print(*old_data, sep='')
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(old_data)


#Вызов функции для изменения данных

    file_choice = int(input("Выберите файл, в который необходимо внести изменения (1 - data_first_variant.csv, 2 - data_second_variant.csv): "))
    if file_choice not in [1, 2]:
        print("Неправильный ввод")
        return
    
    record_to_update = int(input("Введите номер записи, которую хотите обновить: "))
    
    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    if record_to_update > len(lines) or record_to_update <= 0:
        print("Неверный номер записи.")
        return
    updated_record = lines[record_to_update - 1].split()
    
    field_dict = {1: "имя", 2: "фамилия", 3: "телефон", 4: "адрес"}
    field_choice = int(input("Выберите параметр для изменения (1 - имя, 2 - фамилия, 3 - телефон, 4 - адрес): "))
    if field_choice not in field_dict.keys():
        print("Неправильный ввод")
        return
    
    new_value = input("Введите новое значение: ")

    if file_choice == 1:
        with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
            lines = f.readlines()
        if field_choice == 1:
            old_value = name_data()
        elif field_choice == 2:
            old_value = surname_data()
        elif field_choice == 3:
            old_value = phone_data()
        elif field_choice == 4:
            old_value = address_data()
        lines[field_choice - 1] = new_value
        with open('data_first_variant.csv', 'w', encoding='utf-8') as f:
            f.writelines(lines)

    elif file_choice == 2:
        with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
            lines1 = f.readlines()
        data = lines1[0].split(';')
        if field_choice == 1:
            old_value = data[0]
            data[0] = new_value
        elif field_choice == 2:
            old_value = data[1]
            data[1] = new_value
        elif field_choice == 3:
            old_value = data[2]
            data[2] = new_value
        elif field_choice == 4:
            old_value = data[3]
            data[3] = new_value
        new_line = ';'.join(data) + '\n'
        with open('data_second_variant.csv', 'w', encoding='utf-8') as f:
            f.write(new_line)

    print(f"Старое значение {field_dict[field_choice]} было {old_value} Новое значение {field_dict[field_choice]} стало {new_value}")


def delete_data(): 
    var = int(input(f"В каком файле удалить запись?\n\n" 
                    f"1 Вариант (Файл 'data_first_variant.csv'): \n" 
                    f"{'name'}\n{'surname'}\n{'phone'}\n{'address'}\n\n" 
                    f"2 Вариант (Файл 'data_second_variant.csv'): \n" 
                    f"{'name'};{'surname'};{'phone'};{'address'}\n" 
                    f"Выберите вариант: ")) 

    while var != 1 and var != 2: 
        print("Неправильный ввод") 
        var = int(input("Введите число: ")) 

    with open('data_first_variant.csv' if var == 1 else 'data_second_variant.csv', 'r', encoding='utf-8') as f: 
        data_lines = f.readlines() 
        
    data_list = [] 
    j = 0 
    index = 1

    for i in range(len(data_lines)): 
        if data_lines[i] == '\n' or i == len(data_lines) - 1: 
            data_list.append((index, ''.join(data_lines[j:i + 1]))) 
            j = i 
            index += 1
    
    print('\nСписок записей для удаления:\n')
    
    for index, line in data_list:
        print(f"{index}. {line}")
    
    n = int(input("\nКакую запись вы хотите удалить? \nВведите номер записи: ")) 

    data_list.pop(n - 1)
    
    with open('data_first_variant.csv' if var == 1 else 'data_second_variant.csv', 'w', encoding='utf-8') as f: 
        f.writelines([line for _, line in data_list]) 
