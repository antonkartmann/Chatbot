__author__ = "8304676, Kartmann"

import epr_ue_6


def main():
    """
    Dieses Programm erstellt einen Graphen basierend auf den Benutzereingaben und überprüft, ob es sich um einen Baum
    handelt.
    Ein Baum ist ein spezieller Typ von Graph, der bestimmte Eigenschaften erfüllt.

    :return: None
    """
    vertex_list = []  # List to store the nodes

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

    graph_dict = {}  # Dictionary to store the edges
    for element in vertex_list:
        connected_vertices = input(f"Mit welchen Knoten ist {element} verbunden? (Getrennt durch Leerzeichen) ")
        connected_vertices_list = connected_vertices.split()
        graph_dict[element] = connected_vertices_list

    print(f"Der Graph lautet: {graph_dict}")

    # Check if the graph is a tree
    if epr_ue_6.tree_verification(graph_dict):
        epr_ue_6.leaves(graph_dict)
        epr_ue_6.roots(graph_dict)


if __name__ == "__main__":
    main()
