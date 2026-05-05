"""
Estudio : ADA 2026_1 Parcial Practico 2 
Fecha   : 3 Mayo 2026
Nombre  : Miguel Angel Padilla Rosero
Cod     : 8988878

Problem B - Help the Leaders
"""
from sys import stdin

restrictions = set()
words = []
s = 0
solutions = []

def check(candidate, sol):
    ans = True
    for chosen in sol:
        if (chosen, candidate) in restrictions:
            ans = False
    return ans

def backtrack(i, sol):
    global solutions
    if len(sol) == s:
        solutions.append(" ".join(sol))

    elif (len(words) - i >= s - len(sol)):

        for j in range(i, len(words)):
            candidate = words[j]
            isValido = check(candidate, sol)

            if isValido:
                sol.append(candidate)
                backtrack(j + 1, sol)
                sol.pop()

def main():
    global restrictions, words, solutions, s
    casitos = int(stdin.readline())

    for numCase in range(casitos):
        n, p, s = map(int, stdin.readline().split())
        words = []
        restrictions = set()

        for _ in range(n):
            wAux = stdin.readline().strip().upper()
            words.append(wAux)

        for _ in range(p):
            wAux, wAux2 = stdin.readline().split()
            wAux = wAux.upper()
            wAux2 = wAux2.upper()
            restrictions.add((wAux, wAux2))
            restrictions.add((wAux2, wAux))

        words.sort(key=lambda w: (-len(w), w))

        solutions = []
        backtrack(0, [])

        print(f"Set {numCase + 1}:")
        for line in solutions:
            print(line)
        print()


main()


"""
Sample Input
2
8 2 2
WAR
TERROR
PEACE
NUCLEAR-BOMB
HUMAN-RIGHT
FOOD
OIL-CRISIS
EQUAL-RIGHT
WAR OIL-CRISIS
EQUAL-RIGHT NUCLEAR-BOMB
8 0 1
WAR
TERROR
PEACE
NUCLEAR-BOMB
HUMAN-RIGHT
FOOD
OIL-CRISIS
EQUAL-RIGHT
Sample Output
Set 1:
NUCLEAR-BOMB HUMAN-RIGHT
NUCLEAR-BOMB OIL-CRISIS
NUCLEAR-BOMB TERROR
NUCLEAR-BOMB PEACE
NUCLEAR-BOMB FOOD
NUCLEAR-BOMB WAR
EQUAL-RIGHT HUMAN-RIGHT
EQUAL-RIGHT OIL-CRISIS
EQUAL-RIGHT TERROR
EQUAL-RIGHT PEACE
EQUAL-RIGHT FOOD
EQUAL-RIGHT WAR
HUMAN-RIGHT OIL-CRISIS
HUMAN-RIGHT TERROR
HUMAN-RIGHT PEACE
HUMAN-RIGHT FOOD
HUMAN-RIGHT WAR
OIL-CRISIS TERROR
OIL-CRISIS PEACE
OIL-CRISIS FOOD
TERROR PEACE
TERROR FOOD
TERROR WAR
PEACE FOOD
PEACE WAR
FOOD WAR

Set 2:
NUCLEAR-BOMB
EQUAL-RIGHT
HUMAN-RIGHT
OIL-CRISIS
TERROR
PEACE
FOOD
WAR
"""
