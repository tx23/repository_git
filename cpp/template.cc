#include<iostream>
#include<string>
using namespace std;
template<typename T>
void swap1(T &a, T &b) {
    T c = a;
    a = b;
    b = c;
}

int main() {
    int a = 10, b = 11;
    swap1<int>(a, b);
    cout << a << " "<< b << endl;
    string x = "tx";
    string y = "seven";
    swap1(x,y);
    cout << x << " " << y << endl;
}
