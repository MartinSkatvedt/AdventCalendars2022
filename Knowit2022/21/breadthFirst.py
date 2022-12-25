from typing import List
import csv

verticies = []
edges = []

with open("exchange.csv", "r") as f: #Constructs nodes from file
    reader = csv.reader(f)
    for i, line in enumerate(reader):
        if i == 0:
            for j, value in enumerate(line):
                if j == 0 or value == ' ':
                    continue
                verticies.append(value.strip())
            verticies.append("NNOK")
        else:
            for j, value in enumerate(line):
                if j == 0 or value == ' ' or value == ' x':
                    continue
                edges.append([line[0], verticies[j - 1], float(value)])

def edgesStartingWith(curr):
    return filter(lambda x: x[0] == curr, edges)

def alreadyInPath(vertex, path):
    for edge in path:
        if vertex == edge[0]:
            return True
        else:
            return False

def breadthFirstSearch(vertex: str, cost: float, path, depth):
    if vertex == "NOK" and cost > 1.0:
        print(len(path), 1000 *cost) 
        return
    
    if vertex == "NOK" or alreadyInPath(vertex, path) or len(path) >= depth:
        return


    for edge in edgesStartingWith(vertex):
        if edge in path:
            continue
        newPath = path.copy()
        newPath.append(edge)
        breadthFirstSearch(edge[1], cost*edge[2], newPath, depth)

if __name__ == '__main__':
    flag = True
    for depth in range(5, 10):
        for edge in edgesStartingWith("NOK"):
            breadthFirstSearch(edge[1], edge[2], [edge], depth) 
