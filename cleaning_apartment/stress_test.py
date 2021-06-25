import cleaning_apartment
import hamiltonian
import random

tests = 0

while True:
    tests += 1
    print('START TEST {}'.format(tests))
    n = random.randint(3, 30)
    m = random.randint(n//2, n+10)

    edges = []

    for i in range(m):
        u = random.randrange(1, n+1)
        v = random.randrange(1, n+1)
        while u == v:
            v = random.randrange(1, n+1)
        edges.append([u, v])

    print(n, m)
    print(edges)

    cleaning_apartment.printSatFormula(n, m, edges)
    hamiltonian.printSatFormula(n, m, edges)

    ham_out = '/Users/brandonthio/Python/Coursera_DSA/week_3_np_completeness_problems/hamilitonian_out.txt'
    clean_out = '/Users/brandonthio/Python/Coursera_DSA/week_3_np_completeness_problems/clean_apartment_out.txt'
    
    
    with open(ham_out, 'r') as ham:
        with open(clean_out, 'r') as clean:
            correct = ham.readline()
            ans = clean.readline()
      
            if ans != correct:
                print('INCORRECT')
                break