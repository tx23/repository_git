#include <fstream>
#include <iostream>
#include <string>
using namespace std;

int main() {
    ifstream in("text0.txt");
    ofstream out("text.txt");
    string s;
/*    for(int i=0; i<6; ++i) {
        string t;
        cin >> t;
        out << t;
    }
    */
    while (getline(in, s))
        out << s << endl;
    return 0;
}
