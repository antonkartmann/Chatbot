
# old version

# Problem: Sackgasse, im 1. Testfall geht die Funktion zurück zu (0, 0), da alle benachbarten Felder zu dem Zeitpunkt
# den Wert 10 haben.

def greedy_algorithm(matrix):

    """
       Diese Funktion implementiert einen Greedy-Algorithmus, um einen Weg durch eine Matrix zu finden.

       >>> greedy_algorithm([[1, -2, 3], [4, -5, 6], [7, -8, 9]])
       ([(0, 0), (0, 1), (1, 1), (2, 1), (2, 0), (1, 0), (0, 0), (0, 1), (0, 2), (1, 2), (2, 2)], 26)

       >>> greedy_algorithm([[-1, 3, 1], [1, -5, 1], [-4, 2, -9]])
       ([(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)], -13)

       >>> greedy_algorithm([[-2, 3, -9], [0, 5, 9], [3, 3, 3]])
       ([(0, 0), (1, 0), (0, 0), (0, 1), (0, 2), (1, 2), (2, 2)], 2)
       """

    # Create a copy of the matrix
    changeable_matrix = list(matrix)

    # Number of the rows
    rows = len(changeable_matrix)

    # Number of the columns
    columns = len(changeable_matrix[0])

    # List to store the visited elements
    visited_indexes = []

    # Variable to store the current value
    current_value = changeable_matrix[0][0]

    # Add the top left corner of the Matrix to visited_indexes
    visited_indexes.append((0, 0))

    # We create a function that gives back the neighbors an element
    def get_neighbor_values(matrix, index):

        i, j = index[0], index[1]

        neighbor_values = []

        # Add the value of the right element if it exists
        if j + 1 < len(matrix):
            neighbor_values.append((matrix[i][j + 1], (i, j + 1)))

        # Add the value of the bottom element if it exists
        if i + 1 < len(matrix):
            neighbor_values.append((matrix[i + 1][j], (i + 1, j)))

        # Add the value of the left element if it exists
        if j - 1 >= 0:
            neighbor_values.append((matrix[i][j - 1], (i, j - 1)))

        # Add the value of the top element if it exists
        if i - 1 >= 0:
            neighbor_values.append((matrix[i - 1][j], (i - 1, j)))

        return neighbor_values

    # While the current element is not the element in the (n ,n) corner
    while visited_indexes[-1] != (rows - 1, columns - 1):
        # we create a list with every neighbor of current_value
        neighbor_list = get_neighbor_values(changeable_matrix, visited_indexes[-1])

        # use min() to get the neighbor with the smallest value
        smallest_neighbor_value, smallest_neighbor_index = min(neighbor_list)

        # update current_value and add the index to visited_indexes
        current_value += smallest_neighbor_value
        visited_indexes.append(smallest_neighbor_index)

        # update the changeable_matrix to make sure this field won't be visited again
        changeable_matrix[smallest_neighbor_index[0]][smallest_neighbor_index[1]] = 10

    return visited_indexes, current_value