#include <iostream>
#include <ctime>

using namespace std;

int main() {
    time_t *now;
    time(now);
    char *dt = ctime(now);
    cout << "time(0):" << *now << endl 
         << "ctime(now):" << dt << endl;
    return 0;
}
