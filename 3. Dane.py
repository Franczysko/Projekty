#modul csv i msqconnector
import csv
import mysql.connector

with mysql.connector.connect(user='sql11590398', password='kkuJc66NLD', host='sql11.freemysqlhosting.net', database='sql11590398') as connection:
    cursor = connection.cursor()

    with open('C:/Users/frane/Desktop/Program/Python/Projekt/cities.csv') as csvfile:
        reader = csv.DictReader(csvfile)          #DictReader - do wiersza z naglowkami, jesli potem chcemy pokazac kolumny mozemy podac nazwe nazwe kolumny

        for row in reader:
            try:
                Prev_poistion = int(row['2021'])
            except:
                Prev_poistion = 0
            sql = f"""INSERT INTO
            Cities(Name, Country, Position, Prev_poistion)
            VALUES('{row['City']}', '{row['Country']}', {int(row['2022'])} , {Prev_poistion})  
            """
            cursor.execute(sql)
        connection.commit()

 #           print(row['City'])          #wpisujemy nazwe kolumny, a nie jej index poniewam mamy zastosowane DictReader