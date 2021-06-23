with open('/Users/brandonthio/Python/Coursera_DSA/week_3_np_completeness_problems/hamiltonian.txt', 'r') as answer:
    with open('/Users/brandonthio/Python/Coursera_DSA/week_3_np_completeness_problems/clean_apartment.txt', 'r') as attempt:
        ans = answer.readlines()[1:]
        att = attempt.readlines()[1:]

for line in ans:
    if line not in att:
        print(line)

