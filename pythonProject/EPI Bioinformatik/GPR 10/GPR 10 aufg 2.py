__author__ = '8304676, Kartmann'

# Import the regular expression module
import re

# Open and read the file "Wortgitter_mitZahlen.txt" with utf-8 encoding
text = open("Wortgitter_mitZahlen.txt", encoding="utf-8").read()

# i)
# Define a regular expression that looks for patterns starting with a '0', followed by
# any digit (0-9) and a letter (a-z or A-Z)
search_1 = r'0[0-9][a-zA-Z]'

# Search for the first occurrence of the pattern in the text
i_text = re.search(search_1, text)

# Print the first occurrence
print(f"First occurrence: {i_text}")

# ii)
# Find all occurrences of the pattern in the text
search_2 = re.findall(search_1, text)

# Print all occurrences
print(f"All occurrences: {search_2}")

# iii)
# Define a regular expression that looks for expressions consisting of two or three digits
search_3 = r'[0-9]{2,3}'

# Find all occurrences of the pattern in the text
two_or_three_digits = re.findall(search_3, text)

# Print all strings of 2 or 3 numbers that occur
print("All strings of 2 or 3 numbers:", two_or_three_digits)
