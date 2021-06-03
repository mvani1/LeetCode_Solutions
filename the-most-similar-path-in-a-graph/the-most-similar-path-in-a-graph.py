class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:
        path_len = len(targetPath)
        # build graph
        graph = collections.defaultdict(set)
        for road in roads:
            graph[road[0]].add(road[1])
            graph[road[1]].add(road[0])
            
        # since the first city in the path can be any of the n cities, add a
        # fictitious source city -1 to the graph to start from
        graph[-1] = set(range(n))
        
        # in a matrix, keep track of paths of length = path_length (columns)
        # that start from each of the n cities (rows)
        # each mat[row][col] contains the next city following city=row at path_index = col
        next_cities = [[-1] * path_len for _ in range(n)]
        
        # q for BFS
        q = collections.deque()
        # elements in q are tuples (city, path_index)
        # first element is the (fictitious source city, at path index -1)
        q.append((-1, -1))
        
        while q:
            current_city, current_path_index = q.popleft()
            # if we go to the end of the path, build an answer path
            if current_path_index == path_len - 1:
                ans, prev_index = [], path_len - 1
                while prev_index > -1:
                    ans.append(current_city)
                    # the previous city (at the previous index i) in the path
                    current_city = next_cities[current_city][prev_index]
                    prev_index -= 1
                # path was constructed from the last city on path
                return reversed(ans)
            # if we are not at the end of the path just yet, 
            # see what neighbors to visit at next index in the path
            for next_city in graph[current_city]:
                next_tuple = (next_city, current_path_index + 1)
                # don't visit if this city has been considered after the current 
                # at this index
                if next_cities[next_tuple[0]][next_tuple[1]] != -1: continue
                # record that we have been here and where we came from
                next_cities[next_tuple[0]][next_tuple[1]] = current_city
                # Now account for edit distance: it can only be 0 or 1
                if names[next_tuple[0]] == targetPath[next_tuple[1]]:
                    # when edit distance is 0, this city has priority for
                    # visiting next
                    q.appendleft(next_tuple)
                else: # edit distance is 1
                    q.append(next_tuple)
                    
        return []