__author__ = "8304676, Kartmann"


def main():
    """
    Dieses Programm erstellt einen Graphen basierend auf den Benutzereingaben und überprüft, ob es sich um einen Baum
    handelt.
    Ein Baum ist ein spezieller Typ von Graph, der bestimmte Eigenschaften erfüllt.

    :return: None
    """
    vertex_list = []  # Liste zur Speicherung der Knoten

    while True:
        v = input("Wie viele Knoten besitzt Ihr Graph: ")
        if v.isdigit():
            v = int(v)
            break
        else:
            print("Sie müssen eine Ganzzahl eingeben")

    for i in range(v):
        vertex = input("Wie heißt Ihr Knoten? ")
        vertex_list.append(vertex)

    print(f"Die Knoten lauten: {vertex_list}")

    graph_dict = {}  # Dictionary zur Speicherung der Kanten
    for element in vertex_list:
        connected_vertices = input(f"Mit welchen Knoten ist {element} verbunden? (Getrennt durch Leerzeichen) ")
        connected_vertices_list = connected_vertices.split()
        graph_dict[element] = connected_vertices_list

    print(f"Der Graph lautet: {graph_dict}")

    # Überprüfen, ob der Graph ein Baum ist
    if tree_verification(graph_dict):
        print("Bei ihrem Graphen handelt es sich um einen Baum.")
        leaves(graph_dict)
        roots(graph_dict)

    else:
        print("Es handelt sich nicht um einen Baum.")


def tree_verification(dict_of_graph):
    """
    Überprüft, ob der gegebene Graph ein Baum ist.

    :param dict_of_graph: Ein Dictionary, das den Graphen repräsentiert, wie in der Vorlesung.
    :return: True, wenn es sich um einen Baum handelt, sonst False
    """
    # Überprüfen, ob der Graph zusammenhängend ist
    for knoten in dict_of_graph:
        # Überprüfen, ob keine Kanten von dem Knoten ausgehen
        if len(dict_of_graph[knoten]) == 0:
            # Überprüfen, ob keine Kanten zu dem Knoten führen
            for andere_knoten in dict_of_graph:
                if knoten in dict_of_graph[andere_knoten]:
                    break
            else:
                return False

    # Überprüfen, ob G n - 1 Kanten hat.
    number_of_nodes = len(dict_of_graph.keys())
    number_of_edges = sum(len(v) for v in dict_of_graph.values())

    if number_of_nodes - 1 != number_of_edges:

        return False

    return True


def leaves(dict_of_tree):
    """
    Findet die Blätter (Knoten ohne ausgehende Kanten) im gegebenen Baum.

    :param dict_of_tree: Ein Dictionary, das den Baum repräsentiert
    :return: eine Liste der Blätter
    """
    leaves_list = []
    for node in dict_of_tree.keys():
        if len(dict_of_tree[node]) == 0:
            leaves_list.append(node)
    print(f"Die Blätter sind: {leaves_list}")
    return leaves_list


def roots(dict_of_tree):
    """
    Findet die Wurzeln (Knoten ohne eingehende Kanten) im gegebenen Baum.

    :param dict_of_tree: Ein Dictionary, das den Baum repräsentiert
    :return: eine Liste der Wurzeln
    """
    values_set = set()
    roots_list = []

    # Füge alle Werte zu values_set hinzu
    for values in dict_of_tree.values():
        values_set.update(values)

    # Finde Knoten, die keine Werte sind (Wurzeln)
    for node in dict_of_tree.keys():
        if node not in values_set:
            roots_list.append(node)
    if len(roots_list) > 1:
        roots_list = []
    print(f"Die Wurzeln sind: {roots_list}")
    return roots_list


if __name__ == "__main__":
    main()
