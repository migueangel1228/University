"""
Estudio : ADA 2025_2 Tarea 4 
Fecha   : 15 Febrero 2026
Nombre  : Miguel Angel Padilla Rosero
Cod     : 8988878

Problem C - 23 Out of 5
""" 

from sys import stdin
from itertools import permutations

def backtrack(nums, i, acum):
    # Si ya usamos los 5 números, revisamos si llegamos a 23
    if i == 5:
        return acum == 23

    # Probamos las 3 operaciones permitidas
    return (
        backtrack(nums, i + 1, acum + nums[i]) or
        backtrack(nums, i + 1, acum - nums[i]) or
        backtrack(nums, i + 1, acum * nums[i])
    )

def possible(nums):
    # Probar todas las permutaciones
    for perm in permutations(nums):
        # Empezamos con el primer número de la permutación
        if backtrack(perm, 1, perm[0]):
            return True
    return False

def main():
    for line in stdin:
        nums = list(map(int, line.split()))
        if nums == [0, 0, 0, 0, 0]:
            break

        if possible(nums):
            print("Possible")
        else:
            print("Impossible")

main()

"""
Sample Input
1 1 1 1 1
1 2 3 4 5
2 3 5 7 11
0 0 0 0 0
Sample Output
Impossible
Possible
Possible
"""
