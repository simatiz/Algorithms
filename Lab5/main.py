from algorithm import AntColonyAlgorithm
import random as rn
import numpy as np


def create_random_graph(n, min_pow, max_pow, min_dist, max_dist):
    arr = []
    for i in range(n):
        a = []
        for j in range(n):
            if i == j:
                a.append(np.inf)
            else:
                a.append(10000000000000000000)
        power = rn.randint(min_pow, max_pow)
        k = 0
        while k != power:
            a[rn.randint(1, n - 1)] = rn.randint(min_dist, max_dist)
            k += 1
        arr.append(a)
    dist = np.array(arr)
    return dist


def main():
    n_ants = 20
    n_best = 5
    n_iterations = 50
    decay = 0.95
    alpha = 1
    beta = 1
    start = 5
    destination = 155
    min_pow = 1
    max_pow = 10
    min_dist = 5
    max_dist = 150

    distances = create_random_graph(300, min_pow, max_pow, min_dist, max_dist)

    aco = AntColonyAlgorithm(distances, n_ants, n_best, n_iterations, decay, alpha, beta)
    aco.find_shortest_path(start, destination)


if __name__ == "__main__":
    main()
