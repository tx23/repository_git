#include <iostream>
#include <string>
using namespace std;

int main() {
    string name;
    cout << "pls input your name" << endl;
    cin >> name;
    string greeting = "hello, " + name;
    string first(greeting.size()+2, '*');
    string third = '*' + greeting + '*';
    string kongbai(greeting.size(), ' ');
    string second_fourth = '*' + kongbai + '*';
    cout << first << endl << second_fourth << endl 
         << third << endl << second_fourth << endl 
         << first << endl;
    return 0;
}
