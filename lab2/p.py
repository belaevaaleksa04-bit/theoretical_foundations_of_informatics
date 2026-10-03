
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
            return 0

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
    print("крутяк")
