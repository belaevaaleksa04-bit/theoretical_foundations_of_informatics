import os

path = "theoretical_foundations_of_informatics/lab2/data.txt"
if not os.path.exists(path):
    path = "lab2/data.txt"  

with open(path, "r", encoding="utf-8") as file:
    lines = file.readlines()


def unicue_number(file_lines):
    member_number = []
    error = []
    pov = []
    cnt = 0
    for st in file_lines:
        cnt += 1
        raw = st.strip()
        if not raw:
            continue
        parts = raw.split(';')
        if len(parts) < 1:
            continue
        num = parts[0].strip()
        if num not in member_number:
            member_number.append(num)
        else:
            error.append(f"Строка {cnt}: повторяющийся номер участника {num}")
            if num not in pov:
                pov.append(num)
    return error, pov


def check_pole(list_member, number_stroki):
    error = []
    if len(list_member) != 6:
        error.append(f"Строка {number_stroki}: количество полей не равно 6")
    return error


def check_member_number(list_member, number_stroki):
    error = []
    if len(list_member) < 1:
        error.append(f"Строка {number_stroki}: отсутствует номер участника")
        return error
    val = list_member[0].strip()
    if not val.isdigit() or int(val) <= 0:
        error.append(f"Строка {number_stroki}: Номер участника должен быть положительным целым числом")
    return error


def check_name(list_member, number_stroki):
    error = []
    if len(list_member) < 2 or list_member[1].strip() == '':
        error.append(f"Строка {number_stroki}: пустое имя участника")
    return error


def check_group(list_member, number_stroki):
    error = []
    if len(list_member) < 3 or list_member[2].strip() == '':
        error.append(f"Строка {number_stroki}: пустое название группы")
    return error


def check_int_point(list_member, number_stroki):
    error = []
    if len(list_member) != 6:
        return error 
    
    try:
        int(list_member[-1].strip())
        int(list_member[-2].strip())
        int(list_member[-3].strip())
    except ValueError:
        error.append(f"Строка {number_stroki}: балл не целое число")
    return error


def check_diapazon_point(list_member, number_stroki):
    error = []
    if len(list_member) != 6:
        return error
    
    try:
        str1 = int(list_member[-1].strip())
        str2 = int(list_member[-2].strip())
        str3 = int(list_member[-3].strip())
    except ValueError:
        return error  
    if not ((0 <= str1 <= 100) and (0 <= str2 <= 100) and (0 <= str3 <= 100)):
        error.append(f"Строка {number_stroki}: балл должен быть от 0 до 100")
    
    return error  


def last_check(lines):
    all_errors = []
    invalid_numbers = set() 
    cnt = 0

    for stroka in lines:
        cnt += 1
        raw = stroka.strip()

        if not raw:
            continue

        parts = raw.split(';')
        line_errors = []
        line_errors += check_pole(parts, cnt)
        line_errors += check_member_number(parts, cnt)
        line_errors += check_name(parts, cnt)
        line_errors += check_group(parts, cnt)
        line_errors += check_int_point(parts, cnt)
        line_errors += check_diapazon_point(parts, cnt)

        if line_errors:
            all_errors.extend(line_errors)
            invalid_numbers.add(parts[0].strip() if parts else "")

    dup_errors, pov_numbers = unicue_number(lines)
    all_errors.extend(dup_errors)
    

    for num in pov_numbers:
        invalid_numbers.add(num)

    invalid_numbers.discard("")

    return sorted(all_errors), invalid_numbers


def get_category(s):
    if s >= 240:
        return "Отличный результат"
    elif s >= 180:
        return 'Хороший результат'
    elif s >= 120:
        return "Удовлетворительный результат"
    elif s < 120:
        return "Надо подготовиться"
    else:
        return "Ошибка в баллах"


def creation_dict(lines):
    members = {}
    errors, invalid_numbers = last_check(lines)

    for stroka in lines:
        raw = stroka.strip()
        if not raw:
            continue
        
        parts = raw.split(';')
        if len(parts) != 6:
            continue
            
        member_id = parts[0].strip()

        if member_id in invalid_numbers:
            continue

        try:
            itog = int(parts[-1].strip()) + int(parts[-2].strip()) + int(parts[-3].strip())
            sr_itog = round(itog / 3, 2)
            
            members[member_id] = {
                "name": parts[1].strip(),
                "group": parts[2].strip(),
                "points": [int(parts[3].strip()), int(parts[4].strip()), int(parts[5].strip())],
                "final": int(itog),
                "srednee": sr_itog, 
                "category": get_category(itog)
            }
        except ValueError:
            continue

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
        if data["group"].upper().replace(' ', '') == request:
            found = True
            print(f"Участник №{member_id}")
            print(f"  Имя:       {data['name']}")
            print(f"  Группа:    {data['group']}")
            print(f"  Баллы:     {points_str}")
            print(f"  Итог:      {data['final']}")
            print(f"  Среднее:   {data['srednee']}")
            print(f"  Категория: {data['category']}")
    if not found:
        print(f"Никого из группы {request} не найдено")


def find_name(dictionary, request):
    request = request.lower().replace(' ', '')
    found = False
    for member_id, data in dictionary.items():
        points_str = ", ".join(map(str, data["points"]))
        if request in str(data["name"]).lower().replace(' ', ''):
            found = True
            print(f"Участник №{member_id}")
            print(f"  Имя:       {data['name']}")
            print(f"  Группа:    {data['group']}")
            print(f"  Баллы:     {points_str}")
            print(f"  Итог:      {data['final']}")
            print(f"  Среднее:   {data['srednee']}")
            print(f"  Категория: {data['category']}")
    if not found:
        print(f"Никого с частью имени {request} не нашли")
            

def check_prohod(dictionary: dict):
    found = False
    for member_id, data in dictionary.items():
        if int(data["final"]) > 180 and data['points'][0] > 49 and data['points'][1] > 49 and data['points'][2] > 49:
            found = True
            points_str = ", ".join(map(str, data["points"]))
            print(f"Участник №{member_id}")
            print(f"  Имя:       {data['name']}")
            print(f"  Группа:    {data['group']}")
            print(f"  Баллы:     {points_str}")
            print(f"  Итог:      {data['final']}")
            print(f"  Среднее:   {data['srednee']}")
            print(f"  Категория: {data['category']}")
    if not found:
        print("Нет участников, прошедших отбор")


def group_analyse(dictionary: dict):
    groups = {}
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
    errors, invalid_numbers = last_check(lines)
    members = creation_dict(lines)
    
    with open("theoretical_foundations_of_informatics/lab2/tournament_report.txt", 'w', encoding='utf-8') as f:
        f.write("-" * 60 + "\n")
        f.write("Отчет турнира\n")
        f.write("-" * 60 + "\n\n")
        
        total_non_empty = sum(1 for line in lines if line.strip())
        incorrect_count = len(members)
        correct_count = total_non_empty - incorrect_count

        f.write(f"1. Количество корректных записей: {correct_count}\n\n")
        f.write(f"2. Количество некорректных записей: {incorrect_count}\n\n")
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
    
    print("Отчёт сохранён в 'tournament_report.txt'")


def write_group_analyse(dictionary, f):
    groups = {}
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
    if not dictionary:
        f.write("    Нет корректных данных\n\n")
        return
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

members_dict = creation_dict(lines)

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
    
    try:
        choice = int(input("Ваш выбор: "))
    except ValueError:
        print("Выберите число из списка, пожалуйста")
        continue

    if choice == 1:
        names = [data["name"] for data in members_dict.values()]
        print(names)
        print_members(members_dict)
        print('-----')
    elif choice == 2:
        sorted_dict(members_dict)
    elif choice == 3:
        request = input("Участников какой группы ищем? ")
        request = request.upper().replace(' ', '')
        find_group(members_dict, request)
    elif choice == 4:
        question = input("Часть имени кого ищем? ")
        question = question.replace(' ', '')
        find_name(members_dict, question)
    elif choice == 5:
        print("Участники, прошедшие отбор:")
        check_prohod(members_dict)
    elif choice == 6:
        group_analyse(members_dict)
    elif choice == 7:
        otchet(lines)
    elif choice == 0:
        break
    else:
        print("Выберите число из списка, пожалуйста")