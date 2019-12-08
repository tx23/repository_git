#include <iostream>
#include <string>
using namespace std;

int test0() {
    const string hello = "hello";
    const string message = hello + ", world" + "!";
    cout << message << endl;
    {
        const string message = "another sting";
        cout << message << endl;
    };
    return 0;
}

void test1() {
    double middle, final;
    cin >> middle >> final;
    cout << middle << " " << final << endl;
}
void test2() {
    int a = 5/2;
    cout << a << endl;
}

void test3() {
    int *p = 0;
    cout << *p << endl;
    char a[]="tx";
//    char c = a[10];
//    cout << c << endl;
    
}

int main() {
//  test1();
//    test2();
    test3();
    return 0;
}
