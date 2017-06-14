from informed_search import InformedSearch
from eight_puzzle import EightPuzzle

initial_state = EightPuzzle([4, 0, 3,
                            8, 1, 7,
                            5, 2, 6])


goal_state = EightPuzzle([1, 2, 3,
                         4, 5, 6,
                         7, 8, 0])

search = InformedSearch(initial_state, goal_state)
goal_node = search.execute()

if goal_node is None:
    print("Search failed")
else:
    search.show_path(goal_node)
    print(str(search.expanded) + " nodes were expanded!")
