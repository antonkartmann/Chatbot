__author__ = "Kartmann, 8304676"


# Mein Huffman code
huffman_code = {
    'A': '11101',
    'B': '100111',
    'N': '010',
    'O': '1101',
    'E': '1000',
    'R': '1100',
    'U': '0111111',
    'L': '10010',
    'H': '0110',
    'M': '10111',
    'D': '10110',
    'T': '1010',
    'I': '1111',
    'G': '11100',
    'F': '0111110',
    'K': '011110',
    'S': '100110',
    ',': '01110',
    ' ': '00'
}


def encode(message):
    """
    Diese Funktion kodiert eine gegebene Nachricht mit einem Huffman-Code.
    """

    # Initialisiere die kodierte Nachricht als leeren String
    encoded_message = ''

    # Iteriere über jeden Buchstaben in der Nachricht
    for char in message.upper():
        # Wenn der Buchstabe im Huffman-Code-Tabelle ist, füge seinen Code zur kodierten Nachricht hinzu
        if char in huffman_code:
            encoded_message += huffman_code[char]
        else:
            # Wenn der Buchstabe nicht in der Tabelle ist, gib eine Fehlermeldung zurück
            return (f"Fehler: Das Zeichen '{char}' kann nicht kodiert werden, da es nicht in der Huffman-Code-Tabelle "
                    f"ist.")

    # Gib die kodierte Nachricht zurück
    return encoded_message


def decode(encoded_message, huffman_code):
    """
    Diese Funktion decodiert eine Huffman-kodierte Nachricht.
    """

    # Initialisieren der decodierten Nachricht als leeren String
    decoded_message = ''

    # Erstellen einer umgekehrten Huffman-Code-Tabelle
    reverse_huffman_code = {digit: letter for letter, digit in huffman_code.items()}

    # Initialisieren des temporären Codes als leeren String
    temp_code = ''

    # Iteriere über jeden Wert in der kodierte Nachricht
    for code in encoded_message:
        temp_code += code
        # Wenn der temporäre Code in der umgekehrten Huffman-Code-Tabelle ist, füge seinen entsprechenden Buchstaben zur
        # decodierten Nachricht hinzu und setze den temporären Code zurück
        if temp_code in reverse_huffman_code:
            decoded_message += reverse_huffman_code[temp_code]
            temp_code = ''

    # Wenn am Ende der temporäre Code nicht leer ist, gibt er eine Fehlermeldung zurück
    if len(temp_code) > 0:
        return (f"Fehler: Der Code '{temp_code}' kann nicht decodiert werden, da er nicht in der umgekehrten "
                f"Huffman-Code-Tabelle ist.")

    # Dekodierte Nachricht wird zurückgegeben
    return decoded_message


# Testfälle encode:

test_case_1 = encode("Mimoun ist ein G")
test_case_2 = encode("Anton schreibt sicher eine eins")
test_case_3 = encode("Semion ist lash")
test_case_4 = encode("Junkie ist unemployed")
test_case_5 = encode("ein test")

# Testfälle decode:
test_case_6 = decode("1000111101000101010001001101010", huffman_code)  # "ein test" wie erwartet
test_case_7 = decode("001011110001110011101", huffman_code)  # funktioniert wie erwartet
test_case_8 = decode("1001101111011111101111110111111011111101111110111111011111101111110111111",
                     huffman_code)
test_case_9 = decode("1110101010101101010", huffman_code)
test_case_10 = decode("000", huffman_code)


print("Testfälle für die encode() Funktion:")
print(f"Test Fall Nummer 1: {test_case_1}")  # Der Satz wird encoded wie erwartet
print(f"Test Fall Nummer 2: {test_case_2}")  # Wie erwartet kann er den Satz nicht encodieren, da es das C nicht in der
# Tabelle gibt
print(f"Test Fall Nummer 3: {test_case_3}")  # funktioniert wie erwartet
print(f"Test Fall Nummer 4: {test_case_4}")  # Der Satz kann nicht in den Huffman Code umgewnadelt werden, da es j und y
# nicht in der Tabelle gibt
print(f"Test Fall Nummer 5: {test_case_5}")  # Encodierung von "ein test" funktioniert wie erwartet
print("\nTestfälle für die decode() Funktion:")
print(f"Test Fall Nummer 6: {test_case_6}")  # wie erwartet
print(f"Test Fall nummer 7: {test_case_7}")  # wie erwartet
print(f"Test Fall nummer 8: {test_case_8}")  # wie erwartet
print(f"Test Fall nummer 9: {test_case_9}")  # wie erwartet
print(f"Test Fall nummer 10: {test_case_10}")  # wie erwartet, funktioniert nur, wenn die Bits auch den Huffman Code
# wiederspiegeln

# print(encode("One Ring to rule them all, One Ring to find them, One Ring to bring them all, and in the darkness "
#            "bind them"))


