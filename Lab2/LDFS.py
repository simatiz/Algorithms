from func_timeout import func_timeout
from queue import Queue
from puzzle import Puzzle


def ldfs(initial_state, limit):
    return func_timeout(30 * 60, _ldfs, args=[initial_state, limit])

def _ldfs(initial_state, limit):
    start_node = Puzzle(initial_state, None, None, 0)
    Puzzle.iterations = 1

    if start_node.goal_test():
        return True, start_node.find_solution(), 1

    q = Queue()
    q.put(start_node)
    explored = []

    Puzzle.iterations = 0
    while not (q.empty()):
        Puzzle.iterations += 1
        node = q.get()
        explored.append(node.state)

        if node.depth == limit:
            return False, None, len(explored)

        children = node.generate_child()

        for child in children[::-1]:
            if child.state not in explored:
                if child.goal_test():
                    return True, child.find_solution(), len(explored)

                q.put(child)
    return False, None, len(explored)
