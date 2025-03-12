














          es keinen Index - Wert in dem String gibt über 36, da nur 0 - Z zur Verfügung stehen.''')
        # Den Rest als string Wert in die Liste b einfügen
        # Den Rest auf die Variable rest bringen
        # Den Rest der Division durch die Basis finden
        # Den Zahlenwert an den Anfang des Ergebnisses anhängen
        # Den entsprechenden Zahlenwert aus dem String holen
        # Die Dezimalzahl durch die Basis teilen
        # Die Rechenschritte ausgeben
        # Die Rechnung ausgeben mit dem Restwert an der rechten Seite
        # Halben Weg zum Ziel berechnen
        # Zufälligen Eckpunkt auswählen
        # Zur neuen Position gehen und Punkt zeichnen
        # a_2 ohne Rest durch 8 teilen, und den Wert überschreiben
        a_2 = a_2 // 8
        b.append(str(rest))
        neue_position = ((position[0] + zielpunkt[0]) / 2, (position[1] + zielpunkt[1]) / 2)
        position = t.position()
        print("Die Dezimalzahl", x, "umgeschrieben mit der Basis", y, "lautet:", result)
        print("Die Oktalzahl, zu der Dezimalzahl:", a, "lautet:", ergebnis)
        print(f"{a_2} * 8 = Rest = {rest}")
        print(f"{x_2} * {y} = Rest = {zahl}")
        rest = a_2 % 8
        rest = x_2 % y
        result = zahl + result
        return ergebnis
        return ergebnis
        return result
        return result
        t.dot()
        t.goto(neue_position)
        x_2 = x_2 // y
        zahl = zahlenwerte[rest]
        zielpunkt = random.choice(dreieck_punkte)
    # Das Ergebnis als String Wert definieren mit den zahlen der b liste, nur umgekehrt
    # Definieren der Eckpunkte des Dreiecks
    # Ein leerer String, der das Ergebnis speichern wird
    # Eine Schleife, die die Dezimalzahl durch wiederholte Division durch die Basis umwandelt
    # Fenster offen halten
    # Initialisierung der Turtle
    # Iterationen durchführen
    # Leere Liste b erstellen für Reste
    # Setzen der Startposition
    # String mit allen Zahlenwerten
    # Um den Wert a auszugeben am Ende, überschreibe ich den Wert auf a_2
    # Um die Zahlenwerte 0 - Z zuhaben, um so viele Zahlensysteme wie möglich zu inkludieren, erstelle ich einen
    # Wenn die Funktion über das Modul epr_functions ausgeführt wird, wird das Ergebnis ausgegeben
    # Wenn man das modul epr_functions direkt ausführt, wird das Ergebnis ausgegeben
    # Wenn man es über andere module ausführt, wird das Ergebnis zurückgegeben
    # Wenn man es über ein anderes Modul ausführt, wird das Ergebnis nur zurückgegeben
    # While-Schleife erstellen, bis a = 0 ist
    # decimal_to_basis(777777777777777, 100) ==> IndexError: string index out of range
    a_2 = a
    b = []
    chaos_turtle(100, (0, 0))
    decimal_to_basis(1111, 36)
    decimal_to_basis(200, 2)
    decimal_to_octal(100)
    decimal_to_octal(69)
    decimal_to_octal(88)
    dreieck_punkte = [(100, 100), (200, -100), (- 100, -100)]
    else:
    else:
    ergebnis = ''.join(reversed(b))
    for i in range(wiederholungen):
    if __name__ == "__main__":
    if __name__ == "__main__":
    print("Beide Ergebnisse sind wie erwartet.")
    print("Beide Ergebnisse sind wie erwartet.")
    print("Testfall 1:")
    print("Testfall 2:")
    print("Testfall 3:")
    print('''Bei Restwerten über 36, die nur bei Basen > 36 vorkommen können, kommt es zu einem IndexError, da 
    result = ""
    t = turtle.Turtle()
    t.dot()
    t.goto(start_position)
    t.penup()
    turtle.done()
    while a_2 != 0:
    while x_2 != 0:
    x_2 = x
    zahlenwerte = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# Testfall der Funktion chaos_turtle
# Testfälle, nur wenn man das Programm direkt startet
# a)
# b)
__author__ = "8304676, Kartmann"
def chaos_turtle(wiederholungen, start_position):
def decimal_to_basis(x, y):
def decimal_to_octal(a):
if __name__ == "__main__":
if __name__ == "__main__":
import random
import turtle