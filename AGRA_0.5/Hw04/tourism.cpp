/*
AGRA   : Homework 04 - March 2024

AGRA   : Tarea 25 marzo 2025
Nombre : Miguel Angel Padilla Rosero
Cod    : 8988878
B - Problem B tourism.cpp 

Complejidad: 
Complejidad total: O(V + E + V log V) = O(V log V + E)vdonde V es el número de ciudades (vértices) 
y E es el número de carreteras (aristas).

Algoritmo de Tarjan para encontrar componentes fuertemente conectadas O(V + E) 
Encontrar la capital de cada componente O(V)
Construcción del grafo de componentes O(E)Ordenación cola de prioridad: O(V log V)

*/

#include <iostream>
#include <vector>
#include <stack>
#include <string>
#include <unordered_map>
#include <algorithm>
#include <queue>

using namespace std;

struct Node {
    string name;
    int founding;
    bool isCapital;
    int componentIndex;
    
    Node(string name, int founding) {
        this->name = name;
        this->founding = founding;
        this->isCapital = false;
        this->componentIndex = -1;
    }
};
struct Capital {
    int componentIndex;
    string name;
    int founding;
};

struct CapitalComparator {
    bool operator()(const Capital& a, const Capital& b) const {
        bool ans;
        if (a.founding == b.founding)
            ans =  a.name > b.name;
        ans = a.founding > b.founding;

        return ans;
    }
};

// Clase Graphalmacena los nodos, el grafo original y ejecuta TarjanSCC
class Graph {
public:
    int nodeNum;
    vector<Node*> nodeList;
    vector<vector<int>> listaAdj;
    
    Graph(int nodeNum) : nodeNum(nodeNum) {
        listaAdj.resize(nodeNum);
    }
    
    // Agrega una ciudad
    void addNode(string name, int founding) {
        nodeList.push_back(new Node(name, founding));
    }
    
    // Agrega una carretera dirigida entre dos ciudades
    void addEdge(int origin, int destino) {
        listaAdj[origin].push_back(destino);
    }
    
    // Variables para el algoritmo de Tarjan
    vector<int> visitados;
    vector<int> sccIndx;
    vector<bool> enPila;
    stack<int> nodeStack;
    int t;
    int componenteNum;
    vector<vector<int>> components;
    
    // Funcion principal del algoritmo de Tarjan
    void tarjanAlgorithm() {
        visitados.assign(nodeNum, -1);
        sccIndx.assign(nodeNum, -1);
        enPila.assign(nodeNum, false);
        t = 0;
        componenteNum = 0;
        
        for (int i = 0; i < nodeNum; i++) {
            if (visitados[i] == -1) {
                tarjanAux(i);
            }
        }
    }
    
    // Funcion recursiva DFS para Tarjan
    void tarjanAux(int nodeActual) {
        visitados[nodeActual] = sccIndx[nodeActual] = t;
        t++;
        
        nodeStack.push(nodeActual);
        enPila[nodeActual] = true;
        
        // recorre los vecinos del nodo actual
        for (int adjacente : listaAdj[nodeActual]) {
            if (visitados[adjacente] == -1) {
                tarjanAux(adjacente);
                sccIndx[nodeActual] = min(sccIndx[nodeActual], sccIndx[adjacente]);
            } else if (enPila[adjacente]) {
                sccIndx[nodeActual] = min(sccIndx[nodeActual], visitados[adjacente]);
            }
        }
        
        // Si nodeActual es raiz de un componente, extrae todos los nodos de la pila
        if (sccIndx[nodeActual] == visitados[nodeActual]) {
            vector<int> componentActual;
            int nodeIndex;
            bool done = false;
            
            while (!nodeStack.empty() && !done) {
                nodeIndex = nodeStack.top();
                nodeStack.pop();
                enPila[nodeIndex] = false;
                nodeList[nodeIndex]->componentIndex = componenteNum;
                componentActual.push_back(nodeIndex);
                
                if (nodeIndex == nodeActual) {
                    done = true;
                }
            }
            components.push_back(componentActual);
            componenteNum++;
        }
    }
};



int main() {
    
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int testCases;
    cin >> testCases;
    
    while (testCases--) {
        int cityCount, highwayCount;
        cin >> cityCount >> highwayCount;
        
        Graph graph(cityCount);
        unordered_map<string, int> cityIndexMap;
        
        // Lectura de ciudades
        for (int i = 0; i < cityCount; i++) {
            string city;
            int founding;
            cin >> city >> founding;
            graph.addNode(city, founding);
            cityIndexMap[city] = i;
        }
        
        // Lectura de carreteras
        for (int i = 0; i < highwayCount; i++) {
            string originCity, destinationCity;
            cin >> originCity >> destinationCity;
            
            int originIndex = cityIndexMap[originCity];
            int destinationIndex = cityIndexMap[destinationCity];
            
            graph.addEdge(originIndex, destinationIndex);
        }
        
        graph.tarjanAlgorithm();
        
        // Para cada componente, determinar la capital 
        // (la ciudad de fundacion mas antigua; en caso de empate, la de nombre menor)
        vector<Capital> capitalArray(graph.componenteNum);
        
        for (int comparadorNum = 0; comparadorNum < graph.componenteNum; comparadorNum++) {
            
            int capitalCandidateIndx = graph.components[comparadorNum][0];
            
            // recorre los nodos de la componente
            for (int i = 0; i < graph.components[comparadorNum].size(); i++) {


                // obtiene el ind del nodo actual dentro del compont
                int nodeIndex = graph.components[comparadorNum][i];
                
                // obtiene el puntero al nodo actual
                Node* nodeActual = graph.nodeList[nodeIndex];
                
                // Compara la fundacion del nodo actual con el mejor indice encontrado
                // Si el nodo actual tiene una fundacion mas antigua, actualiza el mejor indx
                if ( graph.nodeList[capitalCandidateIndx]->founding > nodeActual->founding ) {
                    capitalCandidateIndx = nodeIndex;
                }
                else if ( graph.nodeList[capitalCandidateIndx]->founding == nodeActual->founding &&
                          nodeActual->name < graph.nodeList[capitalCandidateIndx]->name ) {
                    capitalCandidateIndx = nodeIndex;
                }
            }
            
            capitalArray[comparadorNum] = { comparadorNum, graph.nodeList[capitalCandidateIndx]->name, graph.nodeList[capitalCandidateIndx]->founding };
            graph.nodeList[capitalCandidateIndx]->isCapital = true;
        }
        
        vector<vector<int>> graphSCC(graph.componenteNum);
        vector<int> newEdges(graph.componenteNum, 0);
        
        // recorre todas las ciudades para analizar las conexiones entre componentes
        for (int origin = 0; origin < cityCount; origin++) {
            // recorre las salientes de la ciudad actual
            for (int i = 0; i < graph.listaAdj[origin].size(); i++) {
            // obtiene el indx de la ciudad destino
            int destino = graph.listaAdj[origin][i];
            // obtiene el indx del scc a la que pertenece la ciudad origen
            int comporigin = graph.nodeList[origin]->componentIndex;
            // obtiene el indx de la componente a la que pertenece la ciudad destino
            int compDestination = graph.nodeList[destino]->componentIndex;

                if (comporigin != compDestination) {

                    graphSCC[comporigin].push_back(compDestination);
                    newEdges[compDestination]++;
                }
            }
        }
        
        // ordenacion de las capitales usando una cola de prioridad
        priority_queue<Capital, vector<Capital>, CapitalComparator> capitalPQ;
        
        for (int comparadorNum = 0; comparadorNum < graph.componenteNum; comparadorNum++) {
            if (newEdges[comparadorNum] == 0) {
                capitalPQ.push(capitalArray[comparadorNum]);
            }
        }
        
        vector<string> visitorder; // output
        
        while (!capitalPQ.empty()) {
            Capital currentCapital = capitalPQ.top();
            capitalPQ.pop();
            visitorder.push_back(currentCapital.name);
            
            // revisa las conexiones desde la componente actual
            for (size_t i = 0; i < graphSCC[currentCapital.componentIndex].size(); i++) {
                int nextComp = graphSCC[currentCapital.componentIndex][i];
                newEdges[nextComp]--;
                if (newEdges[nextComp] == 0) {
                    capitalPQ.push(capitalArray[nextComp]);
                }
            }
        }
        
        // Imprimir el orden de visita de las capitales
        for (int i = 0; i < visitorder.size(); i++) {
            cout << visitorder[i];
            bool needSpace = (i + 1 < visitorder.size());
            if (needSpace) {
                cout << " ";
            }
        }
        cout << "\n";
    }
    
    return 0;
}
