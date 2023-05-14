graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0],
]

n = len(graph)
i = 0

def solve(G):
    nodes = [-1]*n
    colours = set()
    for i in range(n):
        colUsed = set()
        for j in range(n):
            if G[i][j] == 1 and nodes[j] != -1:
                colUsed.add(nodes[j])
        if colours - colUsed == set():
            colours.add(i)
            nodes[i] = i
            i+=1
        else: 
            nodes[i] = list(colours-colUsed)[0]
    print(len(colours))

solve(graph)
