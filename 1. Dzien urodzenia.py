import datetime
import calendar

#Translator
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

#Wprowdzaniae danych oraz ich sprawdzanie
print("Podaj date urdozenia w formacie:'DD-MM-YYYY'")

#Sprawdzanie dnia:
data_valid = False
while data_valid == False:
    try:
        day = int(input("Podaj dzien urodzenia: "))
        if day <= 0 or day > 31:       #nasz dzień musi być w zakresie od 1 do 31
            print("Dzień miesiąca pownien byc od 1 do 31")
            continue
        else:
            data_valid = True       #jesli nasza dana bedzie dobra zmienuy wartość data valid na true i nasza petla while sie zmaknie poniewaz tam mielsimy ze data valid == false.
    except:
        print("Dzień miesiąca powinien być liczbą")

#Sprawdzanie miesiąca:
data_valid = False
while data_valid == False:
    try:
        month = int(input("Podaj miesiąc urodzenia: "))
        if month <= 0 or month > 12:       #nasz miesiąc musi być w zakresie od 1 do 12
            print("Miesiąc powinien być od 1 do 12")
            continue
        else:
            data_valid = True      
    except:
        print("Dzień miesiąca powinien być liczbą")

#Sprawdzanie roku:
data_valid = False
while data_valid == False:
    try:
        year = int(input("Podaj rok urodzenia: "))
        if year <= 0 or year > datetime.datetime.now().year:       #nasz rok musi byc większy od 0, jesli usuniemy biezacy rok mozemy w teori spawdzic dzien z przyszłości
            print("Rok powinien być większy od 0 oraz roku bieżacego")
            continue
        else:
            data_valid = True      
    except:
        print("Rok powinien być liczbą")


#Stara metoda
#date_of_birth = input("Podaj date urodzin w formacie dzien-miesiac-rok (np. 1-1-2000): ")
#day, month, year = date_of_birth.split("-")    #split rozdzieli nam nasza date na dzien miesiac i rok.

#Okreslenie dnia oraz jego pokazanie
date_of_birth = datetime.datetime(int(year), int(month), int(day))
day_name = calendar.day_name[date_of_birth.weekday()]

print(translate_to_polish(day_name))
print(translate_to_polish_old_way(day_name))