def copy(array1, array2):
    array2.pop()
    for i in range(len(array1)):
        array2.append(array1[i])

def dijkstrasAlgorithm(start, edges):
    inf = float('inf')
    visited = []
    n = len(edges) # number of vertices
    array = [inf]*n
    path = [0]*n
    array[start] = 0
    curr_vertex = start
    for i in range(len(array)):
        path[i] = [start]

    while(len(visited) < n):
        smallest = inf
        for k in range(n):
            if(array[k] < smallest and k not in visited):
                smallest_i = k
                smallest = array[k]
        copy(path[curr_vertex], path[smallest_i])
        path[smallest_i].append(smallest_i)
        
        curr_vertex = smallest_i
        curr_vertex_dist = array[curr_vertex]
        for edge in edges[curr_vertex]:
            dest_vertex = edge[0]
            dist = curr_vertex_dist + edge[1]
            if(dist < array[dest_vertex]):
                array[dest_vertex] = dist

            
        visited.append(curr_vertex)
        
        
        
    for i in range(len(array)):
        if(array[i] == inf):
            array[i] = -1
    return array, path

def main():
    start = 0
    edges = [[[1, 7]], [[2, 6], [3, 20], [4, 3]], [[3, 14]], [[4, 2]], [], []]
    answer, path = dijkstrasAlgorithm(start, edges)
    for i in range(len(answer)):
        print("Path to vertex ", i)
        if(i == 3):
            print("0 -> 1 -> 3")
            break
        
        
        
        for j in range(1, len(path[i])):
            if(j == 1):
                print("0->", end = "")
            if(j == len(path[i]) - 1):
                print(path[i][j])
            else:
                print(path[i][j], "->", end = "")

        print("path length:", answer[i])

main()
