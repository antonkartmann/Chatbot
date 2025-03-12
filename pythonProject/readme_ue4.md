EPR UE 4 Aufgabe 1

Read me für Datei epr_ue_4.py 

In diesem Programm finden Sie verschiedene Funktionen, die für ein Kartenspiel gedacht sind.

Funktionen
1. create_card_list(a)
Diese Funktion erstellt ein Kartendeck innerhalb einer Liste mit Werten von 1 bis zum Wert von a. Die möglichen 
Kartefarben sind "Pik", "Kreuz", "Herz" und "Karo". Die erstellte Kartenliste wird zurückgegeben.

2. shuffle_card_list(card_list)
Diese Funktion mischt eine bereitgestellte Liste von Karten zufällig. Die gemischte Kartenliste wird zurückgegeben.

3. compare_two_cards(card_one, card_two)
Diese Funktion vergleicht zwei Karten nach ihrem Wert und gibt an, welche Karte den höheren Wert hat. Das Ergebnis
wird als 0 (Karte zwei gewinnt), 1 (Karte eins gewinnt) oder 2 (Unentschieden) zurückgegeben.

4. compare_two_cards_trump(card_one, card_two, trumpf)
Diese Funktion vergleicht zwei Karten unter der Voraussetzung, dass es eine Trumpffarbe gibt, die einen höheren Wert hat 
als die anderen Farben. Das Ergebnis wird im gleichen Stil wie in der Funktion compare_two_cards zurückgegeben.

5. hand_out_cards(list_cards, players, number_of_cards)
Diese Funktion verteilt eine bestimmte Anzahl von Karten an eine bestimmte Anzahl von Spielern. Jeder Spieler erhält
seine eigene Liste von Karten. Die Funktion gibt eine Liste von Spielern zurück.