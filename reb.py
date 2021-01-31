import os

a = int(input('Упрощение жизни: 1)обновление 2)Установка пакета 3)Инъекции '))
if a == 1:
    os.system("apt update")
    os.system("apt full-upgrade")
elif a == 2:
    b = input('Название пакета ')
    os.system("apt-get install " + b)
else: 
    if a == 3:
        a = int(input('1.Nmap(сбор открытых портов) 2.Commix(атака) '))
        if a == 1:
            d = input('url цели ')
            os.system('nmap -u ' + d)
        elif a == 2:
            os.system('python3 ./commix/commix.py')
