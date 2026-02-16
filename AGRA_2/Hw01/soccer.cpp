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

        golesStr1 = partido.substr(posVs -2 -digtsGolesTeam1 +1,  1 +digtsGolesTeam1 -1);
        
        golesStr2 = partido.substr(posVs +4, digtsGolesTeam2 );

        golesInt1 = stoi(golesStr1);
        golesInt2 = stoi(golesStr2);

        namet1 = partido.substr(0,posVs -2 -digtsGolesTeam1);
        namet2 = partido.substr(posVs + 5 +digtsGolesTeam2 ,partido.size() -posVs +4 );

        cout <<  "posVs:" << posVs << " golesStr1:" << golesInt1 << " golesStr2:" << golesInt2 << " namet1:" << namet1 << " namet2:" << namet2 << endl;  
        cout <<  "digtsGolesTeam1:" << digtsGolesTeam1 << " digtsGolesTeam2:" << digtsGolesTeam2 << endl;  


    // Agregar equipos
        if (mapaTeams.find(namet1) == mapaTeams.end()){
            mapaTeams[namet1] = new Team(namet1);
        }
        if (mapaTeams.find(namet2) == mapaTeams.end()){
            mapaTeams[namet2] = new Team(namet2);
        }
    // Actualizar valores equipos
        if (golesInt1 < golesInt2){
            mapaTeams[namet1]->addPoints(0);
            mapaTeams[namet2]->addPoints(3);

            mapaTeams[namet2]->pushTeamDerrotado(mapaTeams[namet1]);
        }
        else if (golesInt1 > golesInt2){
            mapaTeams[namet1]->addPoints(3);
            mapaTeams[namet2]->addPoints(0);

            mapaTeams[namet1]->pushTeamDerrotado(mapaTeams[namet2]);
        }
        else{
            mapaTeams[namet1]->addPoints(1);
            mapaTeams[namet2]->addPoints(1);
        }

        mapaTeams[namet1]->addgoalsDiff(golesInt1 - golesInt2);
        mapaTeams[namet2]->addgoalsDiff(golesInt2 - golesInt1);

        mapaTeams[namet1]->addgoalsScored(golesInt1);
        mapaTeams[namet2]->addgoalsScored(golesInt2);

        mapaTeams[namet2]->addgoalsVisitor(golesInt2);  
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
    int partidos;
    while (cin >> partidos){
        cin.ignore();
        int numParadoxes = 0;
        string partido;
        unordered_map<string,Team*> mapaTeams;

        for (int i = 0; i < partidos; i++){
            getline(cin,partido);
            decodePartido(partido,mapaTeams);
        }

        numParadoxes = paradoxes(mapaTeams);
        unordered_map<string,Team*>::iterator itMap;

        cout << "The paradox occurs "<< numParadoxes <<" time(s)." << endl;

        vector<Team*> vecOrdenPodio;

        for(itMap = mapaTeams.begin(); itMap != mapaTeams.end(); itMap++){
            vecOrdenPodio.push_back(itMap->second);    
        }
        int cnt = 1;
        Team* aux;
        sort(vecOrdenPodio.begin(), vecOrdenPodio.end(),compararEquipos);
        vector<Team*>::iterator itVec;
        for(itVec = vecOrdenPodio.begin(); itVec != vecOrdenPodio.end(); itVec++){
            cout << cnt << ". "<< (*itVec)->getName() << endl;
            cnt++;
        }

    }
    return 0;
}

/*
// Op ternaria =>   condición ? valor_si_verdadero : valor_si_falso;

// Get the iterator of first element of the vector
// vector<int>::iterator it = v.begin();

// Print the content of location which is pointed by iterator (it)
//cout << *it;
*/
/*
SAMPLE IMPUT
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
2
TEAM 1 1 vs. 9 TEAM 2
TEAM 2 15 vs. 8 TEAM 1
7
JSWXKOJAV PDQLPLHPKCFBOPDG 1 vs. 2 IRNESHBALBSFGAYPFF EYHHBMRPSFJXTIXTVJ
GAQZLRN 3 vs. 11 XIC WAX ZTZ FGV ISDKKSYZZVPEUCBTOM
YCM FUPDDPECPVZP BLWUZUDCR RQOPNETKLKRWQFGVVJ 0 vs. 2 IRNESHBALBSFGAYPFF EYHHBMRPSFJXTIXTVJ
XIC WAX ZTZ FGV ISDKKSYZZVPEUCBTOM 0 vs. 5 YCM FUPDDPECPVZP BLWUZUDCR RQOPNETKLKRWQFGVVJ
XIC WAX ZTZ FGV ISDKKSYZZVPEUCBTOM 15 vs. 2 JSWXKOJAV PDQLPLHPKCFBOPDG
JSWXKOJAV PDQLPLHPKCFBOPDG 4 vs. 5 YCM FUPDDPECPVZP BLWUZUDCR RQOPNETKLKRWQFGVVJ
XIC WAX ZTZ FGV ISDKKSYZZVPEUCBTOM 0 vs. 2 IRNESHBALBSFGAYPFF EYHHBMRPSFJXTIXTVJ


SAMPLE OUTPUT
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
The paradox occurs 1 time(s).
1. IRNESHBALBSFGAYPFF EYHHBMRPSFJXTIXTVJ
2. XIC WAX ZTZ FGV ISDKKSYZZVPEUCBTOM
3. YCM FUPDDPECPVZP BLWUZUDCR RQOPNETKLKRWQFGVVJ
4. GAQZLRN
5. JSWXKOJAV PDQLPLHPKCFBOPDG
*/
