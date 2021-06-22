# python3
n, m = map(int, input().split())
edges = [ list(map(int, input().split())) for i in range(m) ]
from itertools import combinations
from collections import defaultdict
import os

def exactly_one_of(literals):
    cnf = [literals] 

    for pair in combinations(literals, 2):
        cnf.append([-l for l in pair])
    
    return cnf

def vertex_appears_in_path(i):
    global n

    cnf = [i+j for j in range(n)]
    # print('RULE 1')
    # print(cnf)
    return cnf

def vertex_appears_once_in_path(i):    

    literals = [i+pos for pos in range(n)]
    
    cnf = exactly_one_of(literals)
    # print('RULE 2')
    # print(cnf)
    
    return cnf

def path_is_occupied(vertices, j):
    cnf = [i+j for i in vertices]
    # print('RULE 3')
    # print(cnf)
    return cnf

def not_two_nodes_same_position(vertices, j):

    literals = [i + j for i in vertices]
    cnf = exactly_one_of(literals)
    
    # print('RULE 4')
    # print(cnf)

    return cnf

def non_adj_vertices(i, k):
    global n
    cnf = []
    # print(i, 'not adjacent to', k)

    for j in range(n-1):
        cnf.append([-(i+j), -(k+j+1)])

    for j in range(n-1, 0, -1):
        cnf.append([-(i+j), -(k+j-1)])

    # print('RULE 5')
    print(cnf)

    return cnf

def adj_vertices(i, adj):
    global n
    cnf = []
    adj_to_i = [(k+1) + (k)*(n-1) for k in range(n) if adj[i][k] == 1]
    i = (i+1) + i*(n-1)

    for j in range(n-1):

        cnf.append([-(i+j)])

        for k in adj_to_i:
            
            cnf[-1].append(k+j+1)

    # print('RULE 5')
    # print(cnf)
    return cnf


def printSatFormula():
    global n

    if m == 0:
        cnf =  [[1], [-1]]
        num_variables = 1
    
    else:
        vertices = [i for i in range(1, n*n, n)]
        num_variables = len(vertices) * n
        adj = [[0 for i in range(n)] for j in range(n)]
        cnf = []

        # print(vertices)

        for (i, k) in edges:
            
            adj[i-1][k-1] = 1
            adj[k-1][i-1] = 1

        for j in range(n):
            
            cnf.append(path_is_occupied(vertices, j))

            cnf.extend(not_two_nodes_same_position(vertices, j))

        
        for i in vertices:

            cnf.append(vertex_appears_in_path(i))

            cnf.extend(vertex_appears_once_in_path(i))

        # pairs = combinations(vertices, 2)
        # for (i, k) in pairs:
        #     if not k in adj[i]:
        #         cnf.extend(non_adj_vertices(i, k))
        
        for i in range(n):
            cnf.extend(adj_vertices(i, adj))

    print("{} {}".format(len(cnf), num_variables))

    for clause in cnf:
        clause.append(0)
        print(' '.join(map(str, clause)))

    # with open('/Users/brandonthio/Python/Coursera_DSA/week_3_np_completeness_problems/temp.txt', 'w+') as temp:

    #     temp.write("p cnf {} {}\n".format(num_variables, len(cnf)))

    #     for clause in cnf:
    #         temp.write('{}\n'.format(' '.join(map(str, clause))))
    
    # os.system('minisat /Users/brandonthio/Python/Coursera_DSA/week_3_np_completeness_problems/temp.txt')

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

printSatFormula()

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