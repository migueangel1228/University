from sys import stdin
from collections import stdin

def crearMapa( n, m, mapa, vecJigglypuff):
    for  r, c, l in vecJigglypuff:
        if (0 <= r < n and 0 <= c < m):
            for i in range(2 * l):
            for j in range(m):
                


def main():
    k = int(input())   # número de Jigglypuff
    listaJigglypuff = []
    for _ in range(k):
        row, col, loudness = map(int, input().split())
        listaJigglypuff.append((row,col,loudness))
    
    n = int(stdin.readline())
    m = n
    # Llenar el mapa
    mapa = []
    for _ in range(n):
            line = stdin.readline()
            mapa.append(line) # mapa de strings
    newMapa = crearMapa(n,m,mapa)
main()



"""
2
2 6 1
7 5 1
7
0000000
00X0000
000X000
0XX0000
0000000
0000000
0000000
Sample Output
12

You are Ash, the famous Pokemon trainer. To become the greatest Pokemon mas-
ter, you travel through regions battling against gym leaders and entering Pokemon
League competitions. With your welltrained Pikachu, Squirtle and Bulbasaur, you
have already captured six badges! What a marvellous performance!
Now, you are walking through the Enchanted Forest, where the most powerful
Pokemons live . . . No, not those giant dragons; we are actually talking about Jiggly-
puffs. A Jigglypuff is a normal-type Balloon Pokemon, with a round, balloon-like
body, a tuft of fur on its forehead, and stubby arms and legs. Whats so powerful of
them? Well, do you notice that microphone in the picture? Thats right, Jigglypuff
has a well-regarded singing voice, and its most popular attack is to sing its oppo-
nent to sleep! Therefore, it is always a good idea to find a route avoiding places
wherever you might hear the Jigglypuffs lullaby.
Let us model the situation as follows: we shall treat the forest as a rectangular
grid.Your starting position is at the top left corner of the grid (1,1), and you will
leave the forest at the lower right corner (R,C). There might be blocked areas which
you are not allowed to trespass through. Jigglypuffs might be present at some cells.
The loudness L of each Jigglypuff is given, which means that places no more than
L units in any direction away from the Jigglypuff are considered “dangerous” and
should be avoided.
Escriba un algoritmo que resuelva este problema. El algoritmo debe recibir el tablero de di-
mensiones R*C y un arreglo de N tripletas (ri,ci,li) que indican las coordenadas (ri,ci) de la
ubicación de cada Jigglypuff en el mapa y su loudness
"""