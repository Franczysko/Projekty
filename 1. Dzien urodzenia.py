import datetime
import calendar

def translate_to_polish(day_name):
    match day_name:
        case 'Monday':
            return 'Poniedzialek'
        case 'Tuesday':
            return 'Wtorek'
        case 'Wednesday':
            return 'Sroda'
        case 'Thursday':
            return 'Czwartek'
        case 'Friday':
            return 'Piatek'
        case 'Saturday':
            return 'Sobota'
        case 'Sunday':
            return 'Niedziela'

def translate_to_polish_old_way(day_name):
    english_to_polish_day_name = {
        'Monday' : 'Poniedzialek',
        'Tuseday' : 'Wtorek',
        'Wednesday' : 'Sroda',
        'Thursday' : 'Czwartek',
        'Friday' : 'Piatek',
        'Saturday' : 'Sobota',
        'Sunday' : 'Niedziela'
    }
    return english_to_polish_day_name[day_name]

date_of_birth = input("Podaj date urodzin w formacie dzien-miesiac-rok (np. 1-1-2000): ")

day, month, year = date_of_birth.split("-")    #split rozdzieli nam nasza date na dzien miesiac i rok.

date_of_birth = datetime.datetime(int(year), int(month), int(day))

day_name = calendar.day_name[date_of_birth.weekday()]

print(translate_to_polish(day_name))
print(translate_to_polish_old_way(day_name))
