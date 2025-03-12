__author__ = "8304676, Kartmann"
from epr_functions import decimal_to_octal, decimal_to_basis, chaos_turtle

# Eingabe, der Nutzer entscheidet, welche Funktion er haben möchte
eingabe = input('''Geben Sie die 1 ein, für die decimal_to_octal Funktion, 
oder die 2 für die decimal_to_basis Funktion, oder die 3 für die chaos_turtle Funktion: ''')

# Wenn die eingabe gültig ist:
if eingabe in ["1", "2", "3"]:

    # Wenn Eingabe = 1, wird der Nutzer um eine Eingabe gebeten, die in der ersten Funktion benutzt wird
    if eingabe == "1":
        dez_zahl_1 = input("Geben Sie bitte die Dezimalzahl an, die umgewandelt werden soll: ")
        dez_zahl_1 = int(dez_zahl_1)
        oct_zahl = decimal_to_octal(dez_zahl_1)
        print("Das Ergebnis lautet:", oct_zahl)

    # Wenn Eingabe = 2, wird der Nutzer um zwei Zahlen gebeten, für die zweite Funktion
    elif eingabe == "2":
        dez_zahl_2 = input("Geben Sie bitte die Dezimalzahl ein: ")
        dez_zahl_2 = int(dez_zahl_2)
        basis = input("Geben Sie bitte die Basis zu der Dezimalzahl an: ")
        basis = int(basis)
        dec_to_bas_zahl = decimal_to_basis(dez_zahl_2, basis)
        print("Das Ergebnis lautet:", dec_to_bas_zahl)

    # Wenn Eingabe = 3, wird der Nutzer zur Eingabe von den Wiederholungen und für den Startpunkt der Turtle gebeten
    elif eingabe == "3":
        wiederholungen_1 = int(input("Geben Sie eine Zahl ein für die Anzahl der Wiederholungen: "))
        # Die Startkoordinaten werden als Liste angenommen. Durch den split Befehl reicht es, wenn sie durch ein
        # Leerzeichen getrennt sind. Außerdem wird durch map(int(.. die int Klasse auf beide Werte angewendet
        start_koordinaten = list(map(int, input('''Geben Sie zwei Zahlen für den Startpunkt der Turtle ein. Die Ziffern
        müssen durch ein Leerzeichen getrennt sein: ''').split()))
        # Die Liste wird nun umgewandelt in ein Tupel, damit es in die Funktion chaos_turtle eingesetzt werden kann
        start_position_1 = (start_koordinaten[0], start_koordinaten[1])
        chaos_turtle(wiederholungen_1, start_position_1)

# Bei einer ungültigen Eingabe, stoppt das Programm und bittet um einen Neustart
else:
    print("Ungültige Eingabe, versuchen Sie es erneut.")




