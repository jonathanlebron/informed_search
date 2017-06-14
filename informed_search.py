import queue


class Node():
    def __init__(self, state, parent, depth, heuristic):
        self.state = state
        self.parent = parent
        self.depth = depth
        self.heuristic = heuristic

    def __str__(self):
        result = "State: " + str(self.state) + "\n"
        result += "Depth: " + str(self.depth) + "\n"
        if self.parent is not None:
            result += "Parent: " + str(self.parent.state)
        return result

    def priority(self):
        return self.depth + self.heuristic

    def __lt__(self, other):
        return self.priority() < other.priority()

    def __gt__(self, other):
        return other.priority() < self.priority()

    def __ge__(self, other):
        return not self.priority() < other.priority

    def __le__(self, other):
        return not other.priority() < self.priority


class InformedSearch():
    def __init__(self, initialState, goalState):
        self.initialState = initialState
        self.goalState = goalState
        self.expanded = 0

    def heuristic(self, node):
        '''Calculate distance from the goal state using Manhattan Distance'''
        h = 0

        for i in range(1, 9):
            tile_index = node.puzzle.index(i)
            expected_tile_index = self.goalState.puzzle.index(i)
            if tile_index != expected_tile_index:
                width = node.n
                row = int(tile_index / width)
                column = tile_index % width
                expected_row = int(expected_tile_index / width)
                expected_column = expected_tile_index % width
                h += abs(row - expected_row) + abs(column - expected_column)
        return h

    def execute(self, verbose=False):
        root = Node(self.initialState, None, 0, self.heuristic(self.initialState))
        visited = set([self.initialState])
        q = queue.PriorityQueue()
        q.put((root.priority(), root))
        cost_treshold = root.heuristic

        while not q.empty():
            p, node = q.get()
            self.expanded += 1
            if self.goalState == node.state:
                return node
            else:
                successors = node.state.apply_operators()
                for state in successors:
                    if state not in visited and self.heuristic(state) < cost_treshold:
                        n = Node(state, node, node.depth+1, self.heuristic(state))
                        q.put((n.priority(), n))
                        visited.add(state)

                cost_treshold += 2

                if verbose:
                    print("Expanded: ", node)
                    print("Number of successors: ", len(successors))
                    print("Queue length: ", q.qsize())
                    print("-------------------------------")

        return None

    def show_path(self, node):
        path = self.build_path(node)
        for node in path:
            print(node.state)
        print("Goal reached in", node.depth, "steps")

    def build_path(self, node):
        """
        Beginning at the goal node, follow the parent links back
        to the start state.  Create a list of the states traveled
        through during the search from start to finish.
        """
        result = []
        while node is not None:
            result.insert(0, node)
            node = node.parent
        return result
