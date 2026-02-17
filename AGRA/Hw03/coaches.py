import sys


"""
AGRA   : Tarea 3 marzo 2025
Nombre : Miguel Angel Padilla Rosero
Cod    : 8988878
b - Problem b - coaches.py

Complejidad programa:

La complejidad temporal del programa en el peor caso es: asignarGeneraciones, que en el peor caso es O(n²) (asumiendo d constante). Las demás partes son O(n log n) y O(k), que quedan por detrás.


"""

class Deportista:
    def __init__(self, nombre, ano):
        self.nombre = nombre
        self.anio_nacimiento = int(ano)
        self.entrenadores = []   # Personas que lo entrenaron
        self.entrenados = []     # Personas a las que entrenó
        self.generacion = None

    def agregar_trainer(self, entrenador):
        self.entrenadores.append(entrenador)

    def agregar_trainee(self, entrenado):
        self.entrenados.append(entrenado)

    def __repr__(self):
        return f"{self.nombre} ({self.anio_nacimiento}) - Gen: {self.generacion}"


class CoachesGraph:
    def __init__(self):
        self.personas = {}

    def agregarPersona(self, nombre, ano):
        if nombre not in self.personas:
            self.personas[nombre] = Deportista(nombre, ano)

    def agregarRelacion(self, entrenador, jugador):
        self.personas[entrenador].agregar_trainee(self.personas[jugador])
        self.personas[jugador].agregar_trainer(self.personas[entrenador])

    def asignarGeneraciones(self):
        # Quienes no tienen entrenadores se les asigna generación 0.
        for p in self.personas.values():
            if not p.entrenadores:
                p.generacion = 0
        cambio = True
        while cambio:
            cambio = False
            for p in self.personas.values():
                if p.generacion is None and p.entrenadores:
                    flag = True
                    for entrenador in p.entrenadores:
                        flag = flag and (entrenador.generacion is not None)
                    if flag:
                        maxGen = None
                        for entrenador in p.entrenadores:
                            if maxGen is None or entrenador.generacion > maxGen:
                                maxGen = entrenador.generacion
                        nuevaGenerari = maxGen + 1
                        p.generacion = nuevaGenerari
                        cambio = True
        resultado = None
        return resultado

    def obtenerMejorCoachGen(self):
        mejorGeneracion = {}
        for p in self.personas.values():
            if (p.generacion is not None) and (len(p.entrenados) != 0):
                gen = p.generacion
                if gen not in mejorGeneracion:
                    mejorGeneracion[gen] = p
                else:
                    actual = mejorGeneracion[gen]
                    if len(p.entrenados) > len(actual.entrenados):
                        mejorGeneracion[gen] = p
                    elif len(p.entrenados) == len(actual.entrenados):
                        if p.anio_nacimiento < actual.anio_nacimiento:
                            mejorGeneracion[gen] = p
                        elif p.anio_nacimiento == actual.anio_nacimiento:
                            if p.nombre < actual.nombre:
                                mejorGeneracion[gen] = p
        resultado = mejorGeneracion
        return resultado


def parse_relationship(tokens, personas):
    result = (None, None)
    i = 1
    while i < len(tokens):
        coach = " ".join(tokens[:i])
        player = " ".join(tokens[i:])
        if coach in personas and player in personas:
            result = (coach, player)
            i = len(tokens)
        else:
            i += 1
    return result


def main():
    salida = None
    entrada = sys.stdin.read().splitlines()
    hecho = False
    if entrada:
        hecho = True
        t = int(entrada[0].strip())
        indice = 1
        for tc in range(1, t + 1):
            n, m = map(int, entrada[indice].split())
            indice += 1
            graph = CoachesGraph()
            for _ in range(n):
                parts = entrada[indice].split()
                indice += 1
                ano = parts[-1]
                nombre = " ".join(parts[:-1])
                graph.agregarPersona(nombre, ano)
            for _ in range(m):
                tokens = entrada[indice].split()
                indice += 1
                coach, player = parse_relationship(tokens, graph.personas)
                
                if coach is not None and player is not None:
                    graph.agregarRelacion(coach, player)
                    
            graph.asignarGeneraciones()
            mejorGeneracion = graph.obtenerMejorCoachGen()
            print(f"Scenario #{tc}:")
            for gen in sorted(mejorGeneracion.keys()):
                print(f"Generation {gen}: {mejorGeneracion[gen].nombre}")
            if tc < t:
                print()
    return salida


main()
