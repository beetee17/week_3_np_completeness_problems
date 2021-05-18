# python3
n, m = map(int, input().split())
edges = [ list(map(int, input().split())) for i in range(m) ]
from itertools import combinations
from collections import defaultdict
import os

## Ruled out: adjacency matrix issue, vertex_appears_in_path func, too many clauses error. Wrong answer on #7

def vertex_appears_in_path(i):
    global n

    cnf = [i+j for j in range(n)]
    cnf.append(0)
    
    return cnf

def vertex_appears_once_in_path(i):    

    cnf = []
    
    for (j1, j2) in combinations(range(n), 2):
        if j1 != j2:
            cnf.append([-(i+j1), -(i+j2), 0])
    
    return cnf

def path_is_occupied(vertices, j):
    cnf = [i+j for i in vertices]
    cnf.append(0)
    return cnf

def not_two_nodes_same_position(vertices, j):

    cnf = []

    for (i, k) in combinations(vertices, 2):

        if i != k:
            cnf.append([-(i+j), -(k+j), 0])

    return cnf

def non_adj_vertices(i, k):
    global n
    cnf = []

    for j in range(n-1):
        cnf.append([-(i+j), -(k+j+1), 0])
    # print(cnf)

    return cnf
def adj_vertices(i, adj):
    global n
    cnf = []
    
    for j in range(n-1):
        cnf.append([-(i+j)])

        for k in adj[i]:
            
            cnf[-1].append(k+j+1)

        cnf[-1].append(0)
    return cnf

# This solution prints a simple satisfiable formula
# and passes about half of the tests.
# Change this function to solve the problem.
def printEquisatisfiableSatFormula():
    global n
    vertices = []
    adj = defaultdict(list)
    cnf = []

    for i in range(1, n*n, n):
        vertices.append(i)

    # print(vertices)

    for (i, k) in edges:

        adj[i+(i-1)*(n-1)].append(k+(k-1)*(n-1))
        adj[k+(k-1)*(n-1)].append(i+(i-1)*(n-1))

    # print(adj)

    for j in range(n):
        
        cnf.append(path_is_occupied(vertices, j))

        cnf.extend(not_two_nodes_same_position(vertices, j))

    
    for i in vertices:

        # cnf.append(vertex_appears_in_path(i))

        cnf.extend(vertex_appears_once_in_path(i))

        cnf.extend(adj_vertices(i, adj))
        # for k in vertices:

            # print(i, (i+n-1)//n -1, k, (k+n-1)//n -1)
            # if not k in adj[i] and i != k:
                # print(i, k)
                # cnf.extend(non_adj_vertices(i, k))
    # print(cnf)
    print("{} {}".format(len(cnf), len(vertices) * n))
   
    for clause in cnf:
        print(' '.join(map(str, clause)))

    with open('temp.txt', 'w+') as temp:

        temp.write("p cnf {} {}\n".format(len(vertices) * n, len(cnf)))

        for clause in cnf:
            temp.write('{}\n'.format(' '.join(map(str, clause))))
    
    os.system('C:\\cygwin\\bin\\minisat.exe C:\\Users\\Admin\\DSA_Course\\week_3_np_completeness_problems\\temp.txt')

# 4 3
# 1 2
# 1 3
# 1 4
# UNSATISFIABLE

    
# 5 4
# 1 2
# 2 3
# 3 5
# 4 5
# SATISFIABLE

printEquisatisfiableSatFormula()

# Each node j must appear in the path.
# • x1j ∨ x2j ∨ · · · ∨ xnj for each j.
# 2. No node j appears twice in the path.
# • ¬xij ∨ ¬xkj for all i, j, k with i =/= k.
# 3. Every position i on the path must be occupied.
# • xi1 ∨ xi2 ∨ · · · ∨ xin for each i.
# 4. No two nodes j and k occupy the same position in the path.
# • ¬xij ∨ ¬xik for all i, j, k with j 6= k.
# 5. Nonadjacent nodes i and j cannot be adjacent in the path.
# • ¬xki ∨ ¬xk+1,j for all (i, j) 6∈ G and k = 1, 2, . . . , n − 1.