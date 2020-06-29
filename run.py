# Search methods

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)

# print(search.breadth_first_graph_search(ab).path())
# print(search.depth_first_graph_search(ab).path())

bnb = search.BandB_graph_search(ab)
print(bnb.path(), "\tVisited:", bnb.visited, "Generated:", bnb.generated)

bnb_sub = search.BandB_Sub_graph_search(ab)
print(bnb_sub.path(), "\tVisited:", bnb_sub.visited, "\tGenerated:", bnb_sub.generated)

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
