import random
from math import sqrt

#Musimy stworzyc pole z x oraz y
game_width = 10
game_height = 10

#Umieszczamy klucz na losowych polach
x_klucza = random.randint(0,game_width)
y_klucza = random.randint(0,game_height)

x_gracza = 0
y_gracza = 0

#Obliczmy odleglosc od klucza do gracza (wzor na pole odcinka)
distance_before_move = sqrt((x_klucza - x_gracza)**2 + (y_klucza - y_gracza)**2)

#Tworzymy zmienną do naszej pętli
player_found_key = False

#Wartośc początkowych kroków
steps = 0 

while not player_found_key:
    steps += 1      #za każdym razem jak wchodzimy do pętli dodajemy jeden krok
    print()
    print("Możesz udać się w kierunkach [W/A/S/D]")

    move = input("Dokąd idziesz? ")
    match move.lower():
        case 'w':
            y_gracza += 1
            if y_gracza > game_height:
                print("Napotykasz ścianę")
                y_gracza = game_height 
        case 's':
            y_gracza -= 1
            if y_gracza < 0:
                print("Napotykasz ścianę")
                y_gracza = 0
        case 'a':
            x_gracza -= 1
            if x_gracza < 0:
                print("Napotykasz ścianę")
                x_gracza = 0
        case 'd':
            x_gracza += 1
            if x_gracza > game_width:
                print("Napotykasz ścianę")  
                x_gracza = game_width
        case 'q':
            print('Koniec gry')
            quit()
        case _:
            print('Nie wiem dokąd idziesz')
            continue

    if x_gracza == x_klucza and y_gracza == y_klucza:
        print("Znalazłeś klucz!")
        print(f"Znalazłeś klucz w {steps} ruchów")
        quit()

    distance_after_move = sqrt((x_klucza - x_gracza)**2 + (y_klucza - y_gracza)**2)

    if distance_before_move > distance_after_move:
        print("Ciepło")
    else:
        print("Zimno")

    distance_before_move = distance_after_move      #nasza poprzednia odleglość jest teraz nową odległością