__author__ = '8304676, Kartmann'


def is_happy(s):
    """
    Checks if a string 's' is happy. A string is considered 'happy' if the frequency of each digit in the string is even

    Args:
    - s (str): The substring to be checked.

    Returns:
    - bool: True if the string is 'happy', False otherwise.
    """
    freq_of_char = {}
    # Counting the frequency of each digit in the string
    for character in s:
        freq_of_char[character] = freq_of_char.get(character, 0) + 1

    # Checking if each digit occurs an even number of times
    for count in freq_of_char.values():
        if count % 2 != 0:
            return False
    return True


def count_happy_substrings(s):
    """
    Counts the number of 'happy' substrings in a given string 's' and returns the corresponding indices of these
    substrings.

    A substring is 'happy' if each digit in it occurs an even number of times.

    Args:
    - s (str): The string in which to search for 'happy' substrings.

    Returns:
    - int: The number of 'happy' substrings.
    - list of tuples: List of indices (l, r) of the 'happy' substrings.
    """
    count = 0
    happy_substrings = []

    # Going through all possible substrings of 's'
    for l in range(len(s)):
        for r in range(l, len(s)):
            # Checking if the current substring is 'happy'
            if is_happy(s[l:r + 1]):
                count += 1
                # Storing the 1-based indices of the 'happy' substring
                happy_substrings.append((l + 1, r + 1))

    return count, happy_substrings

# rekursive Lösung


def count_happy_substrings_recursive(s, start=0, memo=None):
    """
    Recursively counts the number of 'happy' substrings in a given string 's'.
    Utilizes memoization to avoid recalculating for the same substrings.
    """
    if memo is None:
        memo = {}

    if start >= len(s):
        return 0

    if start in memo:
        return memo[start]

    count = 0
    for end in range(start + 1, len(s) + 1):
        if is_happy(s[start:end]):
            count += 1

    # Include the count from the current position and add counts from subsequent positions
    count += count_happy_substrings_recursive(s, start + 1, memo)
    memo[start] = count
    return count


def main():
    """
    Main function for testing the count_happy_substrings function.
    """
    s = ("3141592653589793238462643383279502884197169399375105820974944")
    count, happy_subs = count_happy_substrings(s)
    print(f"Number of 'happy' substrings: {count}")
    print("Indices of the 'happy' substrings:", happy_subs)
    count_recursive = count_happy_substrings_recursive("0112223333444445555556666666777777778888888889999999999")
    print(f"Rekursive indices of the 'happy' substrings: {count_recursive}")


if __name__ == "__main__":
    main()
