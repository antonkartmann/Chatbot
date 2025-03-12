__author__ = "8304676, Kartmann"

'''Dieses Programm untersucht einen Graphen und gibt aus, ob es sich beim Graphen um einen Baum handelt.
Außerdem gibt er noch als Ausgabe die Wurzel und die Blätter des Baumes.'''


def tree_verification(graph_dict):
    """
    Überprüft, ob der gegebene Graph ein Baum ist.

    :param graph_dict: Ein Dictionary, das den Graphen repräsentiert, wie in der Vorlesung.
    :return: True, wenn es sich um einen Baum handelt, sonst False
    """
    # Check if the graph is connected
    for node in graph_dict:
        # Check if no edges go out of the node
        if len(graph_dict[node]) == 0:
            # Check if no edges go to the node
            for other_node in graph_dict:
                if node in graph_dict[other_node]:
                    break
            else:
                print("Es handelt sich nicht um einen Baum")
                return False

    # Check if G has n - 1 edges.
    number_of_nodes = len(graph_dict.keys())
    number_of_edges = sum(len(v) for v in graph_dict.values())

    if number_of_nodes - 1 != number_of_edges:
        print("Es handelt sich nicht um einen Baum")
        return False
    print("Es handelt sich um einen Baum")
    return True


def leaves(tree_dict):
    """
    Findet die Blätter (Knoten ohne ausgehende Kanten) im gegebenen Baum.

    :param tree_dict: Ein Dictionary, das den Baum repräsentiert
    :return: eine Liste der Blätter
    """
    leaves_list = []
    for node in tree_dict.keys():
        if len(tree_dict[node]) == 0:
            leaves_list.append(node)
    print(f"Die Blätter sind: {leaves_list}")
    return leaves_list


def roots(tree_dict):
    """
    Findet die Wurzeln (Knoten ohne eingehende Kanten) im gegebenen Baum.

    :param tree_dict: Ein Dictionary, das den Baum repräsentiert
    :return: eine Liste der Wurzeln
    """
    values_set = set()
    roots_list = []

    # Add all values to values_set
    for values in tree_dict.values():
        values_set.update(values)

    # Find nodes that are not values (roots)
    for node in tree_dict.keys():
        if node not in values_set:
            roots_list.append(node)
    if len(roots_list) > 1:
        roots_list = []
    print(f"Die Wurzeln sind: {roots_list}")
    return roots_list
