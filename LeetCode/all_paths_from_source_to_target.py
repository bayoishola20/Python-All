# Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1, and return them in any order.

# The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

# ALL PATHS FROM SOURCE TO TARGET

class Solution:
    def allPathsSourceTarget(self, graph):
        end = len(graph) - 1
        output = []

        def dfs(curr_node, path, output):
            if curr_node == end:
                output.append(path)
            for next in graph[curr_node]:
                dfs(next, path + [next], output)
        
        dfs(0, [0], output)

        return output

# TIME COMPLEXITY: 

a = Solution()

print( a.allPathsSourceTarget([[1,2],[3],[3],[]]) ) # [[0,1,3],[0,2,3]]

