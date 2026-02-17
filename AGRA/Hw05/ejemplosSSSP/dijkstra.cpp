#include <iostream>
#include <vector>
#include <set>
#include <limits>

using namespace std;

typedef pair<int, int> pii;

void dijkstra(int V, vector<vector<pii>>& adj, int src) {
    vector<int> dist(V, numeric_limits<int>::max());
    set<pii> pq;

    dist[src] = 0;
    pq.insert({0, src});

    while (!pq.empty()) {
        int u = pq.begin()->second;
        pq.erase(pq.begin());

        for (auto& edge : adj[u]) {
            int v = edge.first;
            int weight = edge.second;

            if (dist[u] + weight < dist[v]) {
                if (dist[v] != numeric_limits<int>::max()) {
                    pq.erase({dist[v], v});
                }
                dist[v] = dist[u] + weight;
                pq.insert({dist[v], v});
            }
        }
    }

    for (int i = 0; i < V; ++i) {
        cout << "Distancia desde " << src << " a " << i << " es " << dist[i] << endl;
    }
}

int main() {
    int V = 5; // Número de vértices
    vector<vector<pii>> adj(V);

    // Agregar las aristas (nodo, peso)
    adj[0].push_back({1, 9});
    adj[0].push_back({2, 6});
    adj[1].push_back({2, 2});
    adj[1].push_back({3, 5});
    adj[2].push_back({3, 1});
    adj[3].push_back({4, 3});
    adj[4].push_back({0, 7});

    int src = 0; // Nodo de origen
    dijkstra(V, adj, src);

    return 0;
}
