GPR_UE5_Aufgabe 3

ReadMe für Datei gpr_ue5_aufgabe3

Programmvorstellung:

Dieses Programm sucht unter der Eingabe einer Nadel(needle) und einem Heuhaufen(haystack).
Bei der Verarbeitung des Programms sucht nun das Programm, ab welchem Zeichen die Strings Identich sind.
Hierbei wird, wie man so schön sagt, die Nadel im Heuhaufen gesucht. Das Programm gibt dann bei der Ausgabe, den 
niedrigsten Index an, der bei needle und haystack übereinstimmt.

Zur Benutzung zur Funktion muss man erst einen String für den needle und einen für den haystack ein. 
Die Funktion gibt dann den niedrigsten Index aus, der übereinstimmt. Wenn kein Index übereinstimmt,
gibt die Funktion eine -1 aus.

Testfälle:
1.
Geben Sie die Nadel (needle) ein: Hey
Geben Sie den Heuhaufen (haystack) ein: Hey
Der niedrigste Index, bei dem 'Hey' in 'Hey' auftritt, ist: 0
Das Ergebnis ist wie erwartet.
2.
Geben Sie die Nadel (needle) ein: Hallo
Geben Sie den Heuhaufen (haystack) ein: tschüss
Der niedrigste Index, bei dem 'Hallo' in 'tschüss' auftritt, ist: -1
Das Ergebnis ist erwartet. Keine der zeichen stimmt überein.
3.
Geben Sie die Nadel (needle) ein: Goethe
Geben Sie den Heuhaufen (haystack) ein: Uni Goethe Frankfurt
Der niedrigste Index, bei dem 'Goethe' in 'Uni Goethe Frankfurt' auftritt, ist: 4
Das Ergebnis ist wie erwartet. 

