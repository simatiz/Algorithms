import numpy as np
from numpy.random import choice as np_choice


class AntColonyAlgorithm:
    def __init__(self, distances, n_ants, n_best, n_iterations, decay, alpha=1, beta=1):
        self.distances = distances
        self.n_ants = n_ants
        self.n_best = n_best
        self.n_iterations = n_iterations
        self.decay = decay
        self.alpha = alpha
        self.beta = beta
        self.pheromone = np.ones(distances.shape) / 10
        self.all_inds = range(len(distances))
        self.shortest_path = None
        self.all_time_shortest_path = ("placeholder", np.inf)

    def pick_move(self, pheromone_, dist, visited):
        pheromone = np.copy(pheromone_)
        # Make zero if the path has been visited
        # (can be used to make algorithm faster, but can cause not finding path to destination)
        # pheromone[list(visited)] = 0

        # Ant makes a decision on what node to go using this formula
        row = pheromone ** self.alpha * ((1.0 / dist) ** self.beta)
        # Probability formula
        norm_row = row / row.sum()

        # Move randomly using probability (select path to go using probability)
        # p = probability
        # Get index of an element that has bigger probability
        move = np_choice(self.all_inds, 1, p=norm_row)[0]

        # Return path that randomly selected
        return move

    def spread_pheromone(self, all_paths, n_best):
        # sorted a path form small to big (with values to be shorted are values on second column)
        sorted_paths = sorted(all_paths, key=lambda x: x[1])
        for path, dist in sorted_paths[:n_best]:
            k = 0
            for move in path:
                k += 1
                # print(move)
                # ant deposits a pheromone on the way that its travelled
                # the amount of pheromone that the ant deposit is (1 / distances between 2 cities)
                self.pheromone[move] += 1.0 / self.distances[move]
            print()
            print("Amount of moves: " + str(k))
            print("Distance: {1}\n{0}".format(path, dist))

    def gen_path_dist(self, path):
        total_dist = 0
        for ele in path:
            total_dist += self.distances[ele]
        return total_dist

    def gen_path(self, start, destination):
        path = []
        visited = set()
        visited.add(start)
        prev = start
        move = None
        for i in range(len(self.distances) - 1):
            if move != destination:
                move = self.pick_move(self.pheromone[prev], self.distances[prev], visited)
                # Append path
                path.append((prev, move))
                # Change previous path to move path after append path
                prev = move
                # add path that has been moved to visited, so the path that has visited can be made to zero
                visited.add(move)
            else:
                return path
        return path

    def gen_all_paths(self, start, destination):
        all_paths = []
        for i in range(self.n_ants):
            path = self.gen_path(start, destination)
            all_paths.append((path, self.gen_path_dist(path)))
        return all_paths

    def find_shortest_path(self, start, destination):
        for i in range(self.n_iterations):
            # Get all paths
            all_paths = self.gen_all_paths(start, destination)

            self.spread_pheromone(all_paths, self.n_best)

            # Get the minimal value in array all_paths in column 2
            # example :
            # a = [(0, 8), (3, 7), (2, 6), (1, 9), (4, 5)]
            # min(a, key=lambda x: x[1])
            # the result is : (4, 5)
            # x[1] means second column
            # x[0] means first column
            # shortest path = (path)

            # Get the shortest path in all paths, based on its distance (x[1])
            self.shortest_path = min(all_paths, key=lambda x: x[1])

            # print("shortest path : ## {0}".format(self.shortest_path))

            if self.shortest_path[1] < self.all_time_shortest_path[1]:
                self.all_time_shortest_path = self.shortest_path

            self.pheromone = self.pheromone * self.decay

        k = 0
        for move in self.all_time_shortest_path[0]:
            k += 1

        # return the shortest path that founded by the ants
        print("\nShortest path\n=====================================================================================")
        print("Amount of moves: " + str(k))
        print("Distance: {1}\n{0}".format(self.all_time_shortest_path[0], self.all_time_shortest_path[1]))
        return self.all_time_shortest_path
