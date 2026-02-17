#include <iostream>
#include <string>

using namespace std;

int main() {
    int testCases;
    cin >> testCases;
    int ans = 0;

    while (testCases > 0){
        string operation;
        cin >> operation;
        if (operation[1] == '+'){
            ans++;
        }
        else{
            ans--;
        }
        testCases--;
    }
    cout << ans;


    return 0;

} // MELO 

