# python3
n, m = map(int, input().split())
edges = [ list(map(int, input().split())) for i in range(m) ]

from itertools import combinations, permutations
import os

def vertex_has_one_colour(i):
    # for 3 colour problem -> (a OR b OR c)(a OR b)(a OR c)(b or C)
    # where v(i) is a vertex 
    
    c = combinations(range(3), 2)
    cnf = [[i, i+1, i+2, 0]]

    for c1, c2 in c:
        
        cnf.append([-(i+c1), -(i+c2), 0])
    
    return cnf

def vertices_diff_colour(i, j):
    # NAND gate -> (-a OR -b)

    cnf = []
    for c in range(3):

        cnf.append([-(i+c), -(j+c), 0])

    return cnf

# This solution prints a simple satisfiable formula
# and passes about half of the tests.
# Change this function to solve the problem.
def printEquisatisfiableSatFormula():
    vertices = []
    cnf = []
    for i in range(1, n*3, 3):
        vertices.append(i)

    for i in vertices:
        cnf.extend(vertex_has_one_colour(i))

    for (i, j) in edges:

        cnf.extend(vertices_diff_colour(i+(i-1)*2, j+(j-1)*2))

    print("{} {}".format(len(cnf), len(vertices) * 3))
   
    for clause in cnf:
        print(' '.join(map(str, clause)))

    # with open('temp.txt', 'w+') as temp:

    #     temp.write("p cnf {} {}\n".format(len(vertices) * 3, len(cnf)))

    #     for clause in cnf:
    #         temp.write('{}\n'.format(' '.join(map(str, clause))))
    
    # os.system('C:\\cygwin\\bin\\minisat.exe C:\\Users\\Admin\\DSA_Course\\week_3_np_completeness_problems\\temp.txt')

printEquisatisfiableSatFormula()
