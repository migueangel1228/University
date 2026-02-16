#include <bits/stdc++.h>

using namespace std;

class Team{
    private:
        string name;
        int points = 0;
        int goalsDiff = 0;
        int goalsScored = 0;
        int goalsVisitor = 0;
        vector<Team*> teamsDerrotados;
    public:
    Team(){
    }
    Team(string nombre){
        name = nombre;
    }
    int getPoints(){
        return points;
    }
    int getGoalsDiff(){
        return goalsDiff;
    }
    int getGoalsScored(){
        return goalsScored;
    }
    int getGoalsVisitor(){
        return goalsVisitor;
    }
    string getName(){
        return name;
    }

    vector<Team*> getTeamsDerrotados(){
        return teamsDerrotados;
    }
    Team* atTeamsDerrotados(int pos){
        return teamsDerrotados.at(pos);
    }
    int sizeTeamsDerrotados(){
        return teamsDerrotados.size();
    }
    void pushTeamDerrotado (Team* team){
        teamsDerrotados.push_back(team);
    }

    void addPoints (int p){
        points = points +  p;
    }
    void addgoalsDiff (int p){
        goalsDiff = goalsDiff +  p;
    }
    void addgoalsScored (int p){
        goalsScored = goalsScored +  p;
    }
    void addgoalsVisitor (int p){
        goalsVisitor = goalsVisitor +  p;
    }

    bool operator<(Team &team2){
        if (points != team2.getPoints())
            return points < team2.getPoints();

        else if (goalsDiff != team2.getGoalsDiff()) 
            return goalsDiff < team2.getGoalsDiff();

        else if (goalsScored != team2.getGoalsScored())  
            return goalsScored < team2.getGoalsScored();

        else if (goalsVisitor != team2.getGoalsVisitor())
            return goalsVisitor < team2.getGoalsVisitor();

        else
            return name < team2.getName();
    }
};


void decodePartido(string partido, unordered_map<string,Team*> &mapaTeams){
    int posVs, golesInt1, golesInt2; 
    string golesStr1,golesStr2;
    string namet1, namet2;
    posVs = partido.find('v');
    int digtsGolesTeam1 = 1, digtsGolesTeam2 = 1, cnt;
    bool encontradoDgtsT1 = false, encontradoDgtsT2 = false;

    // Decode del partido(Nombres equipos y goles de cada uno)
        // Revisar posible numero de goles de mas de un digito
        // revisar equipo 1
            cnt = 1;
            while (!encontradoDgtsT1){
                if(partido.substr(posVs -2 -cnt, 1) != " " ){ // (pos - 2) es la posicion del ultimo digito de numero de goles
                    digtsGolesTeam1++;
                }
                else encontradoDgtsT1 = true;
                cnt++;
            }
            cnt = 1;
        // revisar equipo 2
            while (!encontradoDgtsT2){
                if(partido.substr(posVs +4 +cnt, 1) != " " ){ // (pos - 2) es la posicion del ultimo digito de numero de goles
                digtsGolesTeam2++;
                }
                else encontradoDgtsT2 = true;
                cnt++;
            }

        golesStr1 = partido.substr(posVs - 2 - digtsGolesTeam1 + 1,1 + digtsGolesTeam1 - 1 );

        golesStr2 = partido.substr(posVs + 4 + digtsGolesTeam1 - 1,1 + digtsGolesTeam1 + 1 );

        golesInt1 = stoi(golesStr1);
        golesInt2 = stoi(golesStr2);

        namet1 = partido.substr(0,posVs - 3);
        namet2 = partido.substr(posVs + 6 ,partido.size() - posVs + 4 );

        cout <<  "posVs " << posVs << " golesStr1 " << golesInt1 << " golesStr2 " << golesInt2 << " namet1 " << namet1 << " namet2 " << namet2 << endl;  

}

int paradoxes(unordered_map<string, Team*> &mapaTeams) {
    int ans = 0;
    unordered_map<string, Team*>::iterator itMap;
    for (itMap = mapaTeams.begin(); itMap != mapaTeams.end(); itMap++) {
        vector<Team*> derrotados = itMap->second->getTeamsDerrotados();

        vector<Team*>::iterator itVec;
        for (itVec = derrotados.begin(); itVec != derrotados.end(); itVec++) {
            Team* equipo = itMap->second;
            Team* derrotado = *itVec;
            if (*equipo < *derrotado) {
                ans++;
            }
        }
    }
    return ans;
}

// Funcion para ordenar descendentemente usando mi operador '<'
bool compararEquipos(Team* a, Team* b) {
    return *b < *a;
}


int main() {

    //string partido;
    //getline(cin,partido);            
    //solve(partido);
    string s = "la 1234ca";
    string Ssss = s.substr(3,4);
    cout << Ssss << endl;
    int popo = stoi(Ssss);
    cout << popo;
    return 0;
}

/*
Sample Input
13
B. DORTMUND 2 vs. 2 REAL MADRID
SP. PORTUGAL 2 vs. 0 LEGIA
SP. PORTUGAL 1 vs. 2 B. DORTMUND
REAL MADRID 5 vs. 1 LEGIA
B. DORTMUND 1 vs. 0 SP. PORTUGAL
LEGIA 3 vs. 3 REAL MADRID
MONACO 3 vs. 0 CSKA M.
SP. PORTUGAL 1 vs. 2 REAL MADRID
B. DORTMUND 8 vs. 4 LEGIA
REAL MADRID 2 vs. 2 B. DORTMUND
LEGIA 1 vs. 0 SP. PORTUGAL
MONACO 1 vs. 0 SP. PORTUGAL
CSKA M. 1 vs. 0 B. DORTMUND
2
TEAM 1 4 vs. 2 TEAM 2
TEAM 2 2 vs. 0 TEAM 1
Sample Output
The paradox occurs 2 time(s).
1. B. DORTMUND
2. REAL MADRID
3. MONACO
4. LEGIA
5. CSKA M.
6. SP. PORTUGAL
The paradox occurs 1 time(s).
1. TEAM 2
2. TEAM 1
8
*/