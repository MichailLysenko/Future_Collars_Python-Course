'''
def check_whether_user_has_shortened_work_time(users_job):
    return users_job in ['Policjant', 'Strazak', 'Zolnierz'] #zwroci tu wartosc albo true albo false

def check_my_age(users_age, users_job='Programista', *args, *kwargs):
    print(args)
    for argument in args:
        print(argument)
        if argument > 3999:
            print('Masz dobrze platna prace')
    for key, in value in kwargs.items():
        print(f"{key}: {value}")
    #Argument do funkcji (users_age). Tu mamy definicje, a nie wywolanie funkcji, dlatego jest ona podana na poczatku.
    if check_whether_user_has_shortened_work_time(users_job):
        if 18 > users_age:
            return('Nie powinienes jeszcze pracowac')
        elif 18 < users_age < 65:
            return('Jestes w stanie pracowac')
        else:
            return('Jestes w wieku emerytalnym')
    else:
        if users_job == 'Nauczyciel':
            return 'Jestes nauczycielem'
        return 'Nie weszlismy w zaden warunek'

my_job = input('Podaj swoja prace: ')
my_age = int(input('Podaj swoj wiek: '))

if my_job == 'Konserwator':
    displayed_text = check_my_age(my_age, my_job, pensja_konserwatora=4000)
elif my_job == 'Programista':
    displayed_text = check_my_age(my_age, liczba_projektow=24)
elif my_job == 'Nauczyciel':
    displayed_text = check_my_age(my_age, my_job)
else:
    displayed_text = check_my_age(my_age, users_job=my_job)

print(displayed_text)

def check_my_grades(*args):
    for grade in args:
        if grade == 1:
            print('Dostales jedynke')
check_my_grades(1,2,3,1,5,6,3)
'''
#Obiektowosc. Klasy - to polaczenie zmiennych i funkcji
