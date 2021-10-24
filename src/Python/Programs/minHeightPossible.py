"""
you are given the number of node a tree has and the list of edges of the tree, return the min height of the tree possible
input: 
type num_nodes : int
type edges : List[List[int]]
rtype : List[int]
"""

def MinHeightTree(num_nodes: int, edges: List[List[int]]) -> List[int]:
        
        # start with leaves in the list_leaves
        # Remove edges for each leaf - if new leaves form through this process add
        # Repeat this until all the nodes are visited once.
        # return whatever is left in the list_leaves
        
        if num_nodes == 1 or num_nodes==2:
            return [i for i in range(num_nodes)]
        
        adjList = defaultdict(list)
        for e1,e2 in edges:
            adjList[e1].append(e2)
            adjList[e2].append(e1)
          
        visited = [0] * num_nodes
        list_leaves = deque()
        for i in range(num_nodes):
            if len(adjList[i]) == 1: # leaves
                visited[i] = 1
                list_leaves.append(i)
          
        level = 0
        while sum(visited) != num_nodes:
            qlen = len(list_leaves) # Critical to go level by level
            for i in range(qlen): # Critical to go level by level
                leaf = list_leaves.popleft()
                leafNei = adjList[leaf].pop() # only 1 neighbor for leaf
                adjList[leafNei].remove(leaf)
                if len(adjList[leafNei]) == 1:
                    list_leaves.append(leafNei)
                    visited[leafNei] = 1
            level += 1
                    
                
        return list(list_leaves)
