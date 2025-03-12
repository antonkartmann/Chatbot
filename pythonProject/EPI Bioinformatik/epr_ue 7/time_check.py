__author__ = "8304676, Kartmann, 8310275, Nuristani"

import timeit
import epr_ue_7


# We assign the values to the matrix:
test_matrix_1 = [[1, 2], [4, 5]]


# We define the following function:
def check_time(test_matrix: []):
    """
        This function calculates and prints the execution time of two functions:
        'greedy_algorithm' and 'dfs_find_best_path'. Both functions are imported from the module 'epr_ue_7'.
        :param test_matrix: []
    """

    # We calculate the execution time of greedy_algorithm and dfs_find_best_path
    time_greedy_alg = timeit.timeit(lambda: epr_ue_7.greedy_algorithm(test_matrix), number=100000)
    time_dfs_alg = timeit.timeit(lambda: epr_ue_7.dfs_find_best_path(test_matrix), number=100000)

    # We print out the execution times
    print(f"The function Greedy_Algorithm was executed in {time_greedy_alg} seconds.")
    print(f"The function Dfs_find_best_path was executed in {time_dfs_alg} seconds.")


if __name__ == "__main__":
    check_time(test_matrix_1)
