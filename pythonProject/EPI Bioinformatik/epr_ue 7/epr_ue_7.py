__author__ = "8304676, Kartmann, 8310275, Nuristani"


# 1.)
def greedy_algorithm(matrix: []):
    """
    This function implements a greedy algorithm on a given matrix.

    Doctests:
    >>> greedy_algorithm([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    ([(0, 0), (0, 1), (0, 2), (1, 2), (1, 1), (1, 0), (2, 0), (2, 1), (2, 2)], 45)

    >>> greedy_algorithm([[1, 4, -6], [2, 2, 2], [3, 3, -7]])
    ([(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)], 0)

    >>> greedy_algorithm([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
    ([(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)], 21)
    """
    # Number of the rows (Zeilen)
    rows = len(matrix)

    # Number of the columns (Spalten)
    columns = len(matrix[0])

    # List to store the visited elements (Indexes not values)
    visited_indexes = []

    # Variable to store the current value
    current_value = matrix[0][0]

    # Add the top left corner of the Matrix to visited_indexes
    visited_indexes.append((0, 0))

    # We create a function that gives back the neighbors of an element
    def get_neighbor_values(matrix, index):
        i, j = index[0], index[1]
        neighbor_values = []

        # Add the value of the right neighbor if it exists
        if j + 1 < columns:
            neighbor_values.append((matrix[i][j + 1], (i, j + 1)))

        # Add the value of the bottom neighbor if it exists
        if i + 1 < rows:
            neighbor_values.append((matrix[i + 1][j], (i + 1, j)))

        # Add the value of the left neighbor if it exists
        if j - 1 >= 0:
            neighbor_values.append((matrix[i][j - 1], (i, j - 1)))

        # Add the value of the top neighbor if it exists
        if i - 1 >= 0:
            neighbor_values.append((matrix[i - 1][j], (i - 1, j)))

        return neighbor_values

    # While the current element is not the element in the (n ,n) corner
    while visited_indexes[-1] != (rows - 1, columns - 1):

        # we create a list with every neighbor of current_value
        neighbor_list = get_neighbor_values(matrix, visited_indexes[-1])
        # we create a list to find the unvisited neighbors of the current element
        unvisited_neighbors = []

        # If the neighbor of the current element is not in visited_indexes we append it to unvisited_neighbors
        for element in neighbor_list:
            if element[1] not in visited_indexes:
                unvisited_neighbors.append(element)

        # Check if there are any unvisited neighbors left, if not: break
        if len(unvisited_neighbors) == 0:
            break

        # use min() to get the neighbor with the smallest value
        smallest_neighbor_value, smallest_neighbor_index = min(unvisited_neighbors)

        # update current_value and add the index to visited_indexes
        current_value += smallest_neighbor_value
        visited_indexes.append(smallest_neighbor_index)

    return visited_indexes, current_value


# 1.2)

def dfs_find_best_path(matrix: []):  # Tiefensuche
    """
    This function finds the global best path from start to end with the depths first search
    >>> dfs_find_best_path([[-1, 2, -3], [4, -5, 6], [-7, 8, -9]])
    ([(0, 0), (0, 1), (1, 1), (1, 0), (2, 0), (2, 1), (2, 2)], -8)

    >>> dfs_find_best_path([[1, -3, 1], [-1, 5, -1], [4, -2, 1]])
    ([(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)], -1)

    >>> dfs_find_best_path([[-1, 2, -5], [3, -2, 1], [-5, 2, 1]])
    ([(0, 0), (0, 1), (0, 2), (1, 2), (1, 1), (1, 0), (2, 0), (2, 1), (2, 2)], -4)
    """

    def get_neighbor_values(matrix, index):  # Unterfunktion, die die Matrix und den Index entgegennimmt
        i, j = index
        neighbors = []

        # Add the value of the right neighbor if it exists
        if j + 1 < len(matrix[0]):
            neighbors.append((matrix[i][j + 1], (i, j + 1)))

        # Add the value of the bottom neighbor if it exists
        if i + 1 < len(matrix):
            neighbors.append((matrix[i + 1][j], (i + 1, j)))

        # Add the value of the left neighbor if it exists
        if j - 1 >= 0:
            neighbors.append((matrix[i][j - 1], (i, j - 1)))

        # Add the value of the top neighbor if it exists
        if i - 1 >= 0:
            neighbors.append((matrix[i - 1][j], (i - 1, j)))

        return neighbors

    # Recursive function for depth-first search
    def recursive_dfs(matrix, current_position, visited_indexes, current_path, best_path, total_sum, best_sum):
        i, j = current_position

        # Base case: If the current position has reached the bottom right corner
        if current_position == (len(matrix) - 1, len(matrix) - 1):
            # Add the current position to the current path
            current_path.append((i, j))
            # Calculate the sum of the values on the current path
            current_sum = sum(matrix[i][j] for i, j in current_path)

            # Update the best path and best sum if the current path is better
            if current_sum < best_sum[0]:
                best_path[:] = current_path[:]
                best_sum[0] = current_sum

            # Remove the current position from the current path
            current_path.pop()
            return

        # Add the current position to the visited indexes
        visited_indexes.add(current_position)

        # Get the neighbors of the current position
        neighbors = get_neighbor_values(matrix, current_position)

        # Iterate through each neighbor
        for value, next_position in neighbors:  # rekursiver Aufruf
            # Continue the recursive search only in the direction of unvisited neighbors
            if next_position not in visited_indexes:
                current_path.append(current_position)
                recursive_dfs(matrix, next_position, visited_indexes, current_path, best_path, total_sum, best_sum)
                current_path.pop()

        # Remove the current position from the visited indexes
        visited_indexes.remove(current_position)

    # Initialize the best path and best sum with the starting point
    best_path = [(0, 0)]
    best_sum = [999999]

    # Start the recursive search from the top left corner
    recursive_dfs(matrix, (0, 0), set(), [], best_path, 0, best_sum)

    return best_path, best_sum[0]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
