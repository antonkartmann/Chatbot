__author__ = 'Kartmann, 8304676'

# Import the regular expression module
import re

# Open and read the file "Kleopatra.txt" with utf-8 encoding
text = open("Kleopatra.txt", encoding="utf-8").read()

# Use regular expression to replace all occurrences of the word 'sie' with 'er'
new_text = re.sub(r'\bsie\b', 'er', text)

# Print the new text
print(f"Neuer Text: {new_text}")
