file = open("lab2/data.txt", "r", encoding="utf-8")
lines = file.readlines()
def unicue_number(file):
    member_number = []
    error = []
    cnt = 0
    for st in file:
        cnt+=1
        st = st.strip().split(';')
        if st[0] not in member_number:
            member_number.append(st[0])
        else:
            error.append(f"Строка {cnt}: повторяющийся номер участника {st[0]}")
            member_number.append(st[0])
    return error

def check_pole(list_member, number_stroki):
    error = []
    if len(list_member) != 6:
        error.append(f"Строка {number_stroki}: количество полей не равно 6")
    return error

def check_member_number(list_member, number_stroki):
    error = []
    if float(list_member[0])<=0 or not list_member[0].isdigit():
        error.append(f"Строка {number_stroki}: Номер участника должен быть положительным целым числом")
    return error

def check_name(list_member, number_stroki):
    error = []
    if list_member[1]=='':
        error.append(f"Строка {number_stroki}: пустое имя участника")
    return error


def check_group(list_member, number_stroki):
    error = []
    if list_member[2]=='':
        error.append(f"Строка {number_stroki}: пустое название группы")
    return error

def check_int_point(list_member, number_stroki):
    str1 = int(list_member[-1])
    str2 = int(list_member[-2])
    str3 = int(list_member[-3])
    error = []
    if not((isinstance(str1, int)) and (isinstance(str2, int)) and (isinstance(str3, int))):
        error.append(f"Строка {number_stroki}: балл не целое число")
    return error

def check_diapazon_point(list_member, number_stroki):
    str1 = int(list_member[-1])
    str2 = int(list_member[-2])
    str3 = int(list_member[-3])
    error = []
    if (str1>=0 and str1 <101) and (str2>=0 and str2 <101) and (str3>=0 and str3 <101):
        return 1
    else:
        error.append(f"Строка {number_stroki}: балл должен быть от 0 до 100")
        return error

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
    sum_mistakes = list(k1+k2+k3+k4+k5+k6+k7)
    return sorted(sum_mistakes)

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
    sorted_dictionary = sorted(
        dictionary.items(), 
        key=lambda x: (-x[1]["final"], x[1]["name"]), 
    )
    for member_id, data in sorted_dictionary:
        points = ", ".join(map(str, data["points"]))
        print(f"№{member_id} | {data['name']:<20} | Итог: {data['final']} | {data['category']}")

def find_group(dictionary, request):
    found = False
    for member_id, data in dictionary.items():
        points_str = ", ".join(map(str, data["points"]))
        if dictionary[member_id]["group"] == request:
            found = True
            print(f"Участник №{member_id}")
            print(f"  Имя:       {data['name']}")
            print(f"  Группа:    {data['group']}")
            print(f"  Баллы:     {points_str}")
            print(f"  Итог:      {data['final']}")
            print(f"  Среднее:   {data['srednee']}")
            print(f"  Категория: {data['category']}")
    if found == False:
        print(f"Никого из группы {request} не найдено")

def find_name(dictionary = dict, request = str):
    request = request.lower()
    found = False
    for member_id, data in dictionary.items():
            points_str = ", ".join(map(str, data["points"]))
            if request in str(data["name"]).lower().replace(' ', '') :
                found = True
                print(f"Участник №{member_id}")
                print(f"  Имя:       {data['name']}")
                print(f"  Группа:    {data['group']}")
                print(f"  Баллы:     {points_str}")
                print(f"  Итог:      {data['final']}")
                print(f"  Среднее:   {data['srednee']}")
                print(f"  Категория: {data['category']}")
    if found == False:
        print(f"Никого с частью имени {request} не нашли")
            
def check_prohod(dictionary: dict):
    for member_id, data in dictionary.items():
        if int(data["final"]) >180 and data['points'][0]>49 and data['points'][1]>49 and data['points'][2]>49:
            print(f"Участник №{member_id}")
            print(f"  Имя:       {data['name']}")
            print(f"  Группа:    {data['group']}")
            print(f"  Баллы:     {data["points"]}")
            print(f"  Итог:      {data['final']}")
            print(f"  Среднее:   {data['srednee']}")
            print(f"  Категория: {data['category']}")

def group_analyse(dictionary: dict):
    groups = {}  # ключ = название группы, значение = список участников
    for member_id, data in dictionary.items():
        group_name = data["group"]
        if group_name not in groups:
            groups[group_name] = []
        groups[group_name].append({
            "id": member_id,
            "name": data["name"],
            "final": data["final"],
            "points": data["points"],
            "srednee": data["srednee"],
            "category": data["category"]
        })
    for group_name, members in sorted(groups.items()):
        print(f"\n{'='*20}")
        print(f"Группа: {group_name}")
        print(f"{'='*20}")
        count = len(members)
        print(f"Количество участников: {count}")
        finals = [m["final"] for m in members]
        avg = sum(finals) / count
        print(f"Средний итоговый балл: {avg:.2f}")
        max_final = max(finals)
        print(f"Максимальный итоговый балл: {max_final}")
        best_members = [m for m in members if m["final"] == max_final]
        print(f"Участников с максимальным баллом: {len(best_members)}")
        for m in best_members:
            points_str = ", ".join(map(str, m["points"]))
            print(f"  Участник №{m['id']}")
            print(f"    Имя:       {m['name']}")
            print(f"    Группа:    {group_name}")
            print(f"    Баллы:     {points_str}")
            print(f"    Итог:      {m['final']}")
            print(f"    Среднее:   {m['srednee']}")
            print(f"    Категория: {m['category']}")


def otchet(lines):
    errors = last_check(lines)
    members = creation_dict(lines)
    with open("lab2/tournament_report.txt", 'w', encoding='utf-8') as f:
        f.write("-" * 60 + "\n")
        f.write("Отчет турнира\n")
        f.write("-" * 60 + "\n\n")
        f.write(f"1. Количество корректных записей: {len(lines) - len(errors)}\n\n")
        f.write(f"2. Количество некорректных записей: {len(errors)}\n\n")
        f.write("3. Перечень уникальных групп:\n")
        groups = set()
        for data in members.values():
            groups.add(data["group"])
        for group in sorted(groups): 
            f.write(f"   {group}\n")
        f.write("\n")
        f.write("4. Общий рейтинг:\n")
        write_sorted_dict(members, f)  
        f.write("\n")
        f.write("5. Перечень участников, прошедших отбор:\n")
        write_check_prohod(members, f) 
        f.write("\n")
        f.write("6. Статистика по группам\n")
        write_group_analyse(members, f)
        f.write('\n')
        f.write("7. Стастистика по задачам\n")
        write_statistic(members, f)
        f.write("8. Список ошибок входных данных:\n")
        if not errors:
            f.write("   Ошибок нет\n")
        else:
            f.write(f"   Всего обнаружено {len(errors)} ошибок:\n")
            for i, err in enumerate(errors, start=1):
                f.write(f"   {i}. {err}\n")
        
        f.write("\n" + "-" * 60 + "\n")
    
    print(f"Отчёт сохранён в 'tournament_report.txt'")

def write_group_analyse(dictionary, f):
    groups = {}  # ключ = название группы, значение = список участников
    for member_id, data in dictionary.items():
        group_name = data["group"]
        if group_name not in groups:
            groups[group_name] = []
        groups[group_name].append({
            "id": member_id,
            "name": data["name"],
            "final": data["final"],
            "points": data["points"],
            "srednee": data["srednee"],
            "category": data["category"]
        })
    for group_name, members in sorted(groups.items()):
        f.write(f"\n{'-'*20}\n")
        f.write(f"Группа: {group_name}\n")
        f.write(f"{'-'*20}\n")
        count = len(members)
        f.write(f"Количество участников: {count}\n")
        finals = [m["final"] for m in members]
        avg = sum(finals) / count
        f.write(f"Средний итоговый балл: {avg:.2f}\n")
        max_final = max(finals)
        f.write(f"Максимальный итоговый балл: {max_final}\n")
        best_members = [m for m in members if m["final"] == max_final]
        f.write(f"Участников с максимальным баллом: {len(best_members)}\n\n")
        for m in best_members:
            points_str = ", ".join(map(str, m["points"]))
            f.write(f"  Участник №{m['id']}\n")
            f.write(f"    Имя:       {m['name']}\n")
            f.write(f"    Группа:    {group_name}\n")
            f.write(f"    Баллы:     {points_str}\n")
            f.write(f"    Итог:      {m['final']}\n")
            f.write(f"    Среднее:   {m['srednee']}\n")
            f.write(f"    Категория: {m['category']}\n")

def write_statistic(dictionary, f):
    itog = []
    for mem, data in dictionary.items():
        itog.append(data["final"])
    f.write(f"    Средний балл {sum(itog)/len(itog):.2f}\n")
    f.write(f"    Минимальный балл {min(itog)}\n")
    f.write(f"    Максимальный балл {max(itog)}\n")
    f.write('\n')

def write_sorted_dict(dictionary, f):
    sorted_dictionary = sorted(
        dictionary.items(),
        key=lambda x: (-x[1]["final"], x[1]["name"]),
    )
    for member_id, data in sorted_dictionary:
        points = ", ".join(map(str, data["points"]))
        f.write(f"   №{member_id} | {data['name']:<20} | Итог: {data['final']} | {data['category']}\n")


def write_check_prohod(dictionary, f):
    found = False
    for member_id, data in dictionary.items():
        if (data["final"] > 180 and data['points'][0] > 49 and data['points'][1] > 49 and data['points'][2] > 49):
            found = True
            points_str = ", ".join(map(str, data["points"]))
            f.write(f"   Участник №{member_id}\n")
            f.write(f"     Имя:       {data['name']}\n")
            f.write(f"     Группа:    {data['group']}\n")
            f.write(f"     Баллы:     {points_str}\n")
            f.write(f"     Итог:      {data['final']}\n")
            f.write(f"     Среднее:   {data['srednee']}\n")
            f.write(f"     Категория: {data['category']}\n\n")
    
    if not found:
        f.write("   Нет участников, прошедших отбор\n")


while True:
    print('-'*40)
    print('1. Показать всех участников')
    print('2. Показать общий рейтинг')
    print('3. Найти участников по группе')
    print('4. Найти участников по части имени')
    print('5. Показать участников, прошедших отбор')
    print('6. Показать статистику')
    print('7. Сохранить отчёт')
    print('0. Завершить программу')
    print('-'*40)
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
        request = input("Участников какой группы ищем?")
        request = request.upper().replace(' ', '')
        find_group(creation_dict(lines), request)
    elif choice == 4:
        question = input("Часть имени кого ищем?")
        question = question.replace(' ', '')
        find_name(creation_dict(lines), question)
    elif choice == 5:
        print("Участники, прошедшие отбор")
        check_prohod(creation_dict(lines))
    elif choice == 6:
        group_analyse(creation_dict(lines))
    elif choice == 7:
        otchet(lines)
    elif choice == 0:
        break
    else:
        print("Выберете число из списка, пожалуйста")

