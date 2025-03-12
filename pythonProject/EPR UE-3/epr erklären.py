def dfs_find_best_path(matrix: []):
    """
    Findet den global besten Pfad von Start bis Ende mit einer Tiefensuche.
    """

    # Hilfsfunktion, um die Nachbarwerte eines Elements zu bekommen.
    def get_neighbor_values(matrix, index):
    # ... [Die gleiche Logik wie in Ihrer `get_neighbor_values` Funktion] ...

    # Rekursive Funktion für die Tiefensuche.
    def recursive_dfs(matrix, current_position, visited_indexes, current_path, best_path, total_sum, best_sum):
        # Zerlege den aktuellen Index in Zeilen- und Spaltenkomponenten.
        i, j = current_position

        # Überprüfe, ob die rechte untere Ecke erreicht wurde, was das Ende bedeutet.
        if current_position == (len(matrix) - 1, len(matrix[0]) - 1):
            # Füge die aktuelle Position zum Pfad hinzu und berechne die Summe.
            current_path.append((i, j))
            current_sum = sum(matrix[i][j] for i, j in current_path)

            # Aktualisiere den besten Pfad und die beste Summe, falls nötig.
            if current_sum < best_sum[0]:
                best_path[:] = current_path[:]
                best_sum[0] = current_sum

            # Entferne die aktuelle Position vom Pfad und kehre zurück.
            current_path.pop()
            return

        # Füge die aktuelle Position zu den besuchten Indizes hinzu.
        visited_indexes.add(current_position)

        # Ermittle die Nachbarn der aktuellen Position.
        neighbors = get_neighbor_values(matrix, current_position)

        # Durchlaufe jeden Nachbarn für weitere Pfadexploration.
        for value, next_position in neighbors:
            if next_position not in visited_indexes:
                current_path.append(current_position)
                recursive_dfs(matrix, next_position, visited_indexes, current_path, best_path, total_sum, best_sum)
                current_path.pop()

        # Entferne die aktuelle Position aus den besuchten Indizes.
        visited_indexes.remove(current_position)

    # Initialisiere den besten Pfad und die beste Summe.
    best_path = [(0, 0)]
    best_sum = [float('inf')]  # Initialisiere mit Unendlich für Vergleichszwecke.

    # Starte die rekursive Tiefensuche.
    recursive_dfs(matrix, (0, 0), set(), [], best_path, 0, best_sum)

    # Rückgabe des besten Pfades und der besten Summe.
    return best_path, best_sum[0]
