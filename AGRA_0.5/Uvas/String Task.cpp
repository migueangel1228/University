
#include <iostream>
#include <string>
#include <set>
using namespace std;
set<char> vowels{'A', 'O', 'Y', 'E', 'U', 'I','a', 'o', 'y', 'e', 'u', 'i'};
int main() {
    string line;
    cin >> line;
    int ans = 0;

    for (int i = 0; i < line.size(); i++){}
    
        /* code */
    
     (line > 0){
        string operation;
        cin >> operation;
        if (operation[1] == '+'){
            ans++;
        }
        else{
            ans--;
        }
        line--;
    }
    cout << ans;


    return 0;
} // INCOMPLETO


