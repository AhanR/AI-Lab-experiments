
graph = dict()

def solve(key):
    inExploration = [(0,0)]
    explored = [0]
    curr = 0
    seq = []
    while inExploration != []:

        seq.append(curr)

        if curr == key:
            return seq

        for n in graph[curr]:
            if n[1] not in explored and n not in inExploration:
                inExploration.append(n)
        
        # remove the curr and add it to explored
        for i,n in enumerate(inExploration):
            if n[1] == curr:
                explored.append(curr)
                del inExploration[i]
                break
        
        if inExploration == []:
            print(seq)
            print("key not found")
            return False

        # find the cheapest next option
        inExploration.sort()
        minCost = inExploration[0]
        for (c,s) in inExploration:
            if c < minCost[0]:
                minCost = (c,s)
        curr = minCost[1]
    print("key not found")
    return False

def addedge(s,e,c):
    if s not in graph:
        graph[s] = []
    if e not in graph:
        graph[e] = []
    graph[s] += [(c,e)]
    graph[e] += [(c,s)]

addedge(0, 1, 3)
addedge(0, 2, 6)
addedge(0, 3, 5)
addedge(1, 4, 9)
addedge(1, 5, 8)
addedge(2, 6, 12)
addedge(2, 7, 14)
addedge(3, 8, 7)
addedge(8, 9, 5)
addedge(8, 10, 6)
addedge(9, 11, 1)
addedge(9, 12, 10)
addedge(9, 13, 2)
print(solve(11))
