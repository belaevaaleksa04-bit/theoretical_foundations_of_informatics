
file = open("lab2/data.txt", "r", encoding="utf-8")
check_data(file)

def check_data(file): # 1. Проверка данных
    members_number = []
    count = 0
    for stroka in file:
        count+=1
        list_member = stroka.strip().split(';')
        if stroka == "" or len(list_member) == 0:
            print(f'Строка под номером {count} пустая')
        else:
            check_pole(list_member, count) #проверка на 6 полей
            check_member_number(list_member, count) #проверка на номер участника
            if list_member[0] in members_number: # проверка на уникальный номер
                print(f"Строка {count}: повторяющийся номер участника {list_member[0]}")
            else:
                members_number.append(list_member[0])
            check_name(list_member, count) # проверка на пустое имя участника
            check_group(list_member, count) # проверка на пустое название группы
            check_int_point(list_member, count) # целое число баллов
            check_diapazon_point(list_member, count) # диапазон баллов 



def check_pole(list_member, number_stroki):
    if len(list_member) != 6:
        print(f"Строка {number_stroki}: количество полей не равно 6")
    else:
        return 1

def check_member_number(list_member, number_stroki):
    if list_member[0]<=0:
        print(f"Строка {number_stroki}: Номер участника должен быть положительным целым числом")
    else:
        return 1


def check_name(list_member, number_stroki):
    if list_member[1]!='':
        return 1
    else:
        print(f"Строка {number_stroki}: пустое имя участника")


def check_group(list_member, number_stroki):
    if list_member[2]!='':
        return 1
    else:
        print(f"Строка {number_stroki}: пустое название группы")

def check_int_point(list_member, number_stroki):
    str1 = list_member[-1]
    str2 = list_member[-2]
    str3 = list_member[-3]
    if (isinstance(str1, int)) and (isinstance(str2, int)) and (isinstance(str1, int)):
        return 1
    else:
        print(f"Строка {number_stroki}: балл не целое число")

def check_diapazon_point(list_member, number_stroki):
    str1 = list_member[-1]
    str2 = list_member[-2]
    str3 = list_member[-3]
    if (str1 in range(0, 101)) and (str2 in range(0, 101)) and (str3 in range(0, 101)):
        return 1
    else:
        print(f"Строка {number_stroki}: балл должен быть от 0 до 100")

