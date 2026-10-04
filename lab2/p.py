
file = open("lab2/data.txt", "r", encoding="utf-8")
lines = file.readlines()      

def unicue_number(file):
    member_number = []
    cnt = 0
    for st in file:
        cnt+=1
        st = st.strip().split(';')
        if st[0] not in member_number:
            member_number.append(st[0])
        else:
            print(f"Строка {cnt}: повторяющийся номер участника {st[0]}")
            member_number.append(st[0])
            return 0
    if len(member_number) == len(set(member_number)):
        return 1

def check_pole(list_member, number_stroki):
    if len(list_member) != 6:
        print(f"Строка {number_stroki}: количество полей не равно 6")
        return 0
    else:
        return 1

def check_member_number(list_member, number_stroki):
    if float(list_member[0])<=0 or not list_member[0].isdigit():
        print(f"Строка {number_stroki}: Номер участника должен быть положительным целым числом")
        return 0
    else:
       return 1


def check_name(list_member, number_stroki):
    if list_member[1]!='':
        return 1
    else:
        print(f"Строка {number_stroki}: пустое имя участника")
        return 0


def check_group(list_member, number_stroki):
    if list_member[2]!='':
        return 1
    else:
        print(f"Строка {number_stroki}: пустое название группы")
        return 0

def check_int_point(list_member, number_stroki):
    str1 = int(list_member[-1])
    str2 = int(list_member[-2])
    str3 = int(list_member[-3])
    if (isinstance(str1, int)) and (isinstance(str2, int)) and (isinstance(str1, int)):
        return 1
    else:
        print(f"Строка {number_stroki}: балл не целое число")
        return 0

def check_diapazon_point(list_member, number_stroki):
    str1 = int(list_member[-1])
    str2 = int(list_member[-2])
    str3 = int(list_member[-3])
    if (str1>=0 and str1 <101) and (str2>=0 and str2 <101) and (str3>=0 and str3 <101):
        return 1
    else:
        print(f"Строка {number_stroki}: балл должен быть от 0 до 100")
        return 0

def last_check(lines):
    cnt = 0
    for stroka in lines:
        cnt +=1
        stroka = stroka.strip()
        if len(stroka) == "":
            continue
        stroka = stroka.split(';')
        k1 = check_pole(stroka, cnt) #проверка на 6 полей
        k2 = check_member_number(stroka, cnt) #проверка на номер участника
        k3 = check_name(stroka, cnt) # проверка на пустое имя участника
        k4 = check_group(stroka, cnt) # проверка на пустое название группы
        k5 = check_int_point(stroka, cnt) # целое число баллов
        k6 = check_diapazon_point(stroka, cnt) # диапазон баллов 
    k7 = unicue_number(lines)
    if k1 and k2 and k3 and k4 and k5 and k6 and k7:
        print("C входными данными все хорошо")

def get_category(s): #На вход подается сумма баллов
    if s>=240:
        return "Отличный результат"
    elif s>=180:
        return 'Хороший результат'
    elif s>=120:
        return "Удовлетворительный результат"
    elif s<120:
        return "Надо подготовиться"
    else:
        return "Ошибка в баллах"

def creation_dict(lines):
    members = {}
    for stroka in lines:
        stroka = stroka.strip()
        if not stroka:
            continue
        parts = stroka.split(';')
        itog = int(parts[-1]) +int(parts[-2]) +int(parts[-3])
        sr_itog = round(itog/3, 2)
        member_id = parts[0]
        members[member_id] = {
            "name": parts[1],
            "group": parts[2],
            "points": [int(parts[3]), int(parts[4]), int(parts[5])],
            "final": int(itog),
            "srednee": sr_itog, 
            "category": get_category(itog)
        }
    return members

def print_members(members):
    for member_id, data in members.items():
        points_str = ", ".join(map(str, data["points"]))
        print(f"Участник №{member_id}")
        print(f"  Имя:       {data['name']}")
        print(f"  Группа:    {data['group']}")
        print(f"  Баллы:     {points_str}")
        print(f"  Итог:      {data['final']}")
        print(f"  Среднее:   {data['srednee']}")
        print(f"  Категория: {data['category']}")

def sorted_dict(dictionary):
    sorted_dictionary = sorted(dictionary.items(), key=lambda x: x[1]["final"], reverse=True)
    for member_id, data in sorted_dictionary:
        points = ", ".join(map(str, data["points"]))
        print(f"№{member_id} | {data['name']:<20} | Итог: {data['final']} | {data['category']}")



while True:
    last_check(lines)
    print('-----')
    print('1. Показать всех участников')
    print('2. Показать общий рейтинг')
    print('3. Найти участников по группе')
    print('4. Найти участников по части имени')
    print('5. Показать участников, прошедших отбор')
    print('6. Показать статистику')
    print('7. Сохранить отчёт')
    print('0. Завершить программу')
    print('-----')
    choice = int(input())
    if choice == 1:
        members = []
        for i in lines:
            stroka = i.strip().split(';')
            if len(stroka)!=0:
                members.append(stroka[1])
        print(members)
        print_members(creation_dict(lines))
        print('-----')
    elif choice == 2:
        sorted_dict(creation_dict(lines))
    elif choice == 3:
        ... 
    elif choice == 4:
        ...
    elif choice == 5:
        ...
    elif choice == 6:
        ...
    elif choice == 7:
        ...
    elif choice == 0:
        break
    else:
        print("Выберете число из списка, пожалуйста")


