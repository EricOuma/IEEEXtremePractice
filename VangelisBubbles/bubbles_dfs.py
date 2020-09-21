#!usr/bin/python3
from collections import defaultdict
import random

def helper(edges):
    d = defaultdict(list)
    for k, v in edges:
        d[k].append(v)
        d[v].append(k)
    return d


def dfs(edges, start, visited):
    for n in edges[start]:
        if n not in visited:
            visited.add(n)
            dfs(edges, n, visited)

def loop_checker(edges, start, visited):
    for n in edges[start]:
        if n not in visited:
            visited.add(n)
            loop_checker(edges, n, visited)
        else: # if n in visited
            if len(visited) > 2:
                return 1
    return 0


def work(filename):
    cycles = []
    with open(filename) as f:
        test_cases = int(f.readline())
        for _ in range(test_cases):
            visited  = set()
            n, m = f.readline().split(' ')
            temp = f.readline().rstrip().split(' ')
            vertices = sorted(list(set(temp)))
            i = 0
            pairs = []
            for _ in range(int(m)):
                pairs.append(temp[i:i+2])
                i += 2
            edges = helper(pairs)
            start = random.choice(vertices)
            visited.add(start)
            cycles.append(loop_checker(edges, start, visited))
    with open("output.txt", "a") as output:
        [output.write(f"{n}\n") for n in cycles]

work("input.txt")