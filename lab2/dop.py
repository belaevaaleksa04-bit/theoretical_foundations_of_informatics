file = open("lab2/data.txt", "r", encoding="utf-8")
lines = file.readlines()
while True:
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
    elif choice == 2:
        ...

