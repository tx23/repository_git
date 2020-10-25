#include <iostream>
using namespace std;

int work (int x) {
    int i = x/2 -1;
    return i;
}
int main() {
    int i=0;
    cout << "pls input a number" << endl;
    cin >> i;
    for(int j = 1; j<=10; ++j) 
        i=work(i);
    cout << i << endl;
    return 0;
}
