# University

Repositorio académico de algoritmos, programación competitiva y estructuras de datos. Aquí conviven soluciones de tareas, parciales, ejercicios de juez en línea, ejemplos de clase y material de apoyo para cursos como `ADA`, `AGRA`, `AGRA_2` y `PreADA`.

Más que un proyecto único, este repo funciona como una bitácora técnica de aprendizaje: muestra evolución, comparación de enfoques, práctica constante y resolución de problemas en Python y C++.

## Qué vas a encontrar aquí

- Soluciones independientes para problemas de programación competitiva y tareas universitarias.
- Implementaciones de técnicas clásicas como divide and conquer, programación dinámica, DFS/BFS, Dijkstra, Bellman-Ford, Floyd-Warshall, Tarjan, Kosaraju, Kruskal, Prim y Union-Find.
- Casos de prueba en archivos `.in` y `.out`.
- Enunciados, libros, PDFs de apoyo y apuntes.
- Algunos ejecutables, archivos temporales y notas rápidas generadas durante la práctica.

## Estructura del repositorio

```text
University/
|-- PreADA/
|-- ADA/
|   |-- Docs/
|   |-- hw01/
|   |-- hw02/
|   |-- hw03/
|   |-- mt01/
|   |-- notes/
|   `-- Study/
|-- AGRA/
|   |-- Hw01/ ... Hw06/
|   |-- Mt01_Op/
|   |-- proyect/
|   `-- Uvas/
`-- AGRA_2/
    |-- Hw01/ ... Hw06/
    |-- PreParcial1/
    |-- PreParcial2/
    |-- Preparcial3/
    |-- Proyecto/
    |-- Invariantes/
    `-- docs/
```

## Mapa por carpetas

- `PreADA`: entrenamiento previo y problemas clásicos de jueces en línea. Predominan grafos implícitos, BFS, shortest paths y MST en contextos tipo laberinto o grillas.
- `ADA`: trabajo de Análisis y Diseño de Algoritmos. Aquí aparecen tareas por módulos (`hw01`, `hw02`, `hw03`), un parcial (`mt01`), material bibliográfico y ejercicios de estudio.
- `AGRA`: trabajo de Árboles y Grafos. Incluye tareas numeradas, ejemplos de algoritmos sobre grafos, problemas de conectividad, caminos mínimos, SCC y MST.
- `AGRA_2`: segunda etapa del trabajo en grafos. Amplía el repertorio con preparciales, variantes de soluciones, práctica adicional y un proyecto final con documentación.

## Temas técnicos dominantes

- Divide and conquer: closest pair, recurrencias, estrategias de partición.
- Programación dinámica: coin change, knapsack, optimización por estados, memoización y tabulación.
- Grafos implícitos: mazes, rutas, ascensores, movimiento en grillas.
- Shortest paths: BFS, Dijkstra, Bellman-Ford, DAG SSSP y Floyd-Warshall.
- Conectividad y componentes: DFS, SCC, puntos de articulación y puentes.
- Árboles de expansión mínima: Kruskal, Prim y estructuras disjoint-set.
- Estructuras de apoyo: heaps, pilas, colas, diccionarios, segment trees y grafos por lista de adyacencia.

## Archivos representativos

- `PreADA/KillingAliensInBorgMaze.py`: mezcla de BFS sobre grafo implícito con Kruskal para construir una solución tipo MST.
- `ADA/hw01/pair.py`: closest pair usando divide and conquer.
- `ADA/hw02/ingredients.py`: combinación de optimización sobre DAG de recetas y knapsack.
- `ADA/hw03/change.py`: variante de making change con DP para cliente y cálculo de cambio del cajero.
- `AGRA/Hw04/critical.py`: búsqueda de puntos de articulación con recorrido DFS tipo Tarjan.
- `AGRA/Hw05/ejemplosSSSP/`: carpeta valiosa para repasar familias de shortest path.
- `AGRA_2/hw04/`: práctica de SCC, puentes y articulaciones.
- `AGRA_2/Hw06/zlatan.cpp`: solución más grande y compuesta, con SCC, Dijkstra y lógica adicional sobre componentes.
- `AGRA_2/Proyecto/Final.tex`: ejemplo de documentación formal de un proyecto final.

## Cómo ejecutar soluciones

La mayoría de archivos son programas standalone: leen desde `stdin` y escriben a `stdout`. No hay un sistema único de build ni dependencias externas grandes; casi todo usa biblioteca estándar.

### Python

Ejecutar un script directamente:

```powershell
python ADA\hw03\change.py
```

Ejecutar con un archivo de entrada desde PowerShell:

```powershell
cmd /c "python ADA\hw03\change.py < ADA\hw03\_samples\change.in"
```

Otro ejemplo:

```powershell
cmd /c "python ADA\hw01\pair.py < ADA\hw01\_samples\pair.in"
```

### C++

Compilar un archivo:

```powershell
g++ AGRA\Hw06\mst\prim.cpp -std=c++17 -O2 -o prim.exe
```

Compilar y ejecutar con entrada:

```powershell
cmd /c "g++ AGRA\Hw04\dominos.cpp -std=c++17 -O2 -o dominos.exe && dominos.exe < AGRA\Hw04\_samples\dominos.in"
```

## Convenciones que aparecen en el repo

- `_samples/`: entradas y salidas de referencia de una tarea.
- `.in` y `.out`: casos de prueba locales.
- `docs/` o PDFs sueltos: enunciados, teoría o bibliografía.
- `output/`: binarios o resultados generados durante pruebas.
- `popo*.txt`, `prueba*`, `temp*`: archivos rápidos de experimentación o depuración.

## Cómo recorrer el repositorio sin perderse

- Si quieres ver progresión técnica: empieza en `PreADA`, sigue con `ADA` y luego entra a `AGRA`.
- Si quieres revisar solo grafos: ve directo a `AGRA/Hw03` en adelante y luego compara con `AGRA_2`.
- Si quieres repasar algoritmos concretos: usa los ejemplos de `AGRA/Hw04/Ejemplos`, `AGRA/Hw05/ejemplosSSSP` y `AGRA/Hw06/mst`.
- Si te interesa la parte más formal del trabajo: revisa `AGRA_2/Proyecto`, `ADA/Docs` y los PDFs de cada homework.

## Lo que hace fuerte a este repo

- Muestra continuidad real de estudio, no solo entregas aisladas.
- Reúne teoría, práctica, pruebas y documentación en un mismo lugar.
- Permite comparar múltiples versiones de una misma idea entre materias y semestres.
- Tiene valor como portafolio académico y también como banco personal de referencia.

## Estado actual del repositorio

Este repositorio tiene una identidad clara de laboratorio académico. La prioridad aquí ha sido resolver, practicar y documentar, no empaquetar todo bajo una sola convención de ingeniería. Por eso es normal encontrar nombres pragmáticos, ejecutables ya compilados, archivos de prueba mezclados con código final y varias versiones de un mismo problema.

Eso no le quita valor: al contrario, lo vuelve un archivo honesto del proceso de aprendizaje. Si en algún momento quieres llevarlo a una versión más presentable para portafolio público, el siguiente paso natural sería añadir un `.gitignore`, limpiar binarios, normalizar nombres y crear `README` por materia.

## Uso esperado

- Consulta académica personal.
- Repaso antes de parciales o entregas.
- Reutilización de plantillas de algoritmos.
- Base para comparar soluciones entre Python y C++.

## Nota final

Si alguien abre este repo por primera vez, la mejor forma de leerlo es como una colección organizada por cursos y problemas, no como una aplicación monolítica. Cada carpeta cuenta una etapa distinta del proceso de formación en algoritmos.
