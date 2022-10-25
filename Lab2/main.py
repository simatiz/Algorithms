from time import time
from LDFS import ldfs
from RBFS import rbfs
from puzzle import Puzzle


def main():
    state = [[0, 1, 2,
              3, 4, 5,
              6, 7, 8],

             [3, 1, 2,
              4, 7, 5,
              0, 6, 8],

             [6, 3, 2,
              0, 1, 5,
              7, 4, 8],

             [1, 0, 5,
              3, 2, 4,
              6, 7, 8],

             [1, 4, 2,
              3, 7, 5,
              6, 0, 8],

             [3, 1, 0,
              4, 5, 2,
              6, 7, 8],

             [3, 1, 2,
              6, 4, 0,
              7, 8, 5],

             [1, 4, 2,
              3, 0, 5,
              6, 7, 8],

             [1, 4, 2,
              6, 3, 5,
              0, 7, 8],

             [1, 2, 5,
              6, 3, 4,
              7, 8, 0],

             [3, 2, 5,
              4, 7, 1,
              0, 6, 8],

             [1, 2, 5,
              3, 0, 8,
              6, 4, 7],

             [3, 1, 0,
              6, 4, 2,
              7, 8, 5],

             [3, 1, 2,
              0, 4, 5,
              6, 7, 8],

             [3, 0, 2,
              6, 1, 5,
              7, 4, 8],

             [0, 4, 2,
              1, 7, 5,
              3, 6, 8],

             [3, 1, 0,
              4, 5, 2,
              6, 7, 8],

             [3, 1, 2,
              6, 4, 5,
              7, 0, 8],

             [1, 2, 5,
              3, 4, 8,
              6, 7, 0],

             [3, 0, 1,
              4, 7, 2,
              6, 8, 5]]

    limit = 100000

    for i in range(20):
        print('-----------------------------------------------------')
        print('Test number:', i + 1)
        print()
        try:
            Puzzle.num_of_states = 0
            Puzzle.iterations = 0
            t0 = time()
            flag, LDFS, states_in_memory = ldfs(state[i], limit)
            t1 = time()
            t = t1 - t0

            if not flag:
                print("Couldn't find solution")
                print('Iterations:', Puzzle.iterations)
                print('Number of states:', Puzzle.num_of_states)
                print('States stored in memory:', states_in_memory)
                print('Time:', t)
                print()
            else:
                print('LDFS:', LDFS)
                print('Iterations:', Puzzle.iterations)
                print('Number of states:', Puzzle.num_of_states)
                print('States stored in memory:', states_in_memory)
                print('Time:', t)
                print()
        except:
            print("Timeout")
            print('Iterations:', Puzzle.iterations)
            print('Number of states:', Puzzle.num_of_states)
            print('States stored in memory:', states_in_memory)
            print('Time:', t)
            print()

        try:
            Puzzle.num_of_states = 0
            Puzzle.iterations = 0
            t0 = time()
            RBFS = rbfs(state[i])
            t1 = time()
            t = t1 - t0

            print('RBFS:', RBFS)
            print('Iterations:', Puzzle.iterations)
            print('Number of states:', Puzzle.num_of_states)
            print('States stored in memory:', Puzzle.states_in_memory)
            print('Time:', t)
            print()
        except:
            print("Timeout")
            print('Iterations:', Puzzle.iterations)
            print('Number of states:', Puzzle.num_of_states)
            print('States stored in memory:', Puzzle.states_in_memory)
            print('Time:', t)
            print()

if __name__ == "__main__":
    main()
