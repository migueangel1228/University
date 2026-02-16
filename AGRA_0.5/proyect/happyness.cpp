#include <iostream>
#include <vector>
#include <queue>
#include <climits>
using namespace std;

struct Edge {
    int to;
    long long cost;
};

// Custom comparator for priority queue
struct CompareNode {
    bool operator()(const pair<int, long long>& a, const pair<int, long long>& b) {
        return a.second > b.second;  // Min-heap based on days worked
    }
};

int main() {
    int t;
    cin >> t;
    
    while (t--) {
        int n, m;
        long long initial_money, doll_cost;
        cin >> n >> m >> initial_money >> doll_cost;
        
        vector<long long> earn_per_day(n + 1);
        for (int i = 1; i <= n; i++) {
            cin >> earn_per_day[i];
        }
        
        int start, end;
        cin >> start >> end;
        
        // Adjacency list to represent the graph
        vector<vector<Edge>> graph(n + 1);
        
        for (int i = 0; i < m; i++) {
            int u, v;
            long long c;
            cin >> u >> v >> c;
            graph[u].push_back({v, c});
        }
        
        // Money left after buying the doll
        long long money_left = initial_money - doll_cost;
        
        // Minimum days needed to reach each city
        vector<long long> min_days(n + 1, LLONG_MAX);
        min_days[start] = 0;
        
        // Priority queue to implement Dijkstra's algorithm
        // Pair: (city, days_worked)
        priority_queue<pair<int, long long>, vector<pair<int, long long>>, CompareNode> pq;
        pq.push({start, 0});
        
        // To track how much money Kenny has when reaching each city with minimum days
        vector<long long> money_at_city(n + 1, -1);
        money_at_city[start] = money_left;
        
        while (!pq.empty()) {
            int city = pq.top().first;
            long long days = pq.top().second;
            pq.pop();
            
            if (days > min_days[city]) continue;
            
            // Try all outgoing edges from the current city
            for (const Edge& edge : graph[city]) {
                int next_city = edge.to;
                long long ticket_cost = edge.cost;
                long long current_money = money_at_city[city];
                
                // Calculate how many days Kenny needs to work to afford the ticket
                long long days_needed = 0;
                if (current_money < ticket_cost) {
                    // Calculate days needed to earn enough money
                    long long money_needed = ticket_cost - current_money;
                    days_needed = (money_needed + earn_per_day[city] - 1) / earn_per_day[city]; // Ceiling division
                }
                
                // Calculate new total days and money after working and traveling
                long long new_days = days + days_needed;
                long long new_money = current_money + (days_needed * earn_per_day[city]) - ticket_cost;
                
                if (new_days < min_days[next_city]) {
                    min_days[next_city] = new_days;
                    money_at_city[next_city] = new_money;
                    pq.push({next_city, new_days});
                } else if (new_days == min_days[next_city] && new_money > money_at_city[next_city]) {
                    // If same days but more money, update
                    money_at_city[next_city] = new_money;
                    pq.push({next_city, new_days});
                }
            }
        }
        
        // Check if Kenny can reach the destination
        if (min_days[end] == LLONG_MAX) {
            cout << "Sorry Kenny, Happiness is not for you :(" << endl;
        } else {
            cout << "Kenny happiness will cost " << min_days[end] << " days of work :)" << endl;
        }
    }
    
    return 0;
}