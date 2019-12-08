#include <iostream>
#include <vector>
using std::cout;
using std::vector;
using std::endl;

vector<vector<int> > result;

void combination(int n, int k, int start, vector<int> c) {
    //int j = k;
    if(c.size() == k) {
        result.push_back(c);
        return;
    }
    
    for(int i = start; i <= n; ++i) {
        c.push_back(i);
        combination(n, k, i+1, c);
        c.pop_back();
    }
}
    //int answer[k];
    
int main() {
    int n = 4;
    int k = 2;
    vector<int> c;
   // n++;
    combination(n, k, 1, c);
//    cout << result;
    for(int i = 0; i < result.size(); ++i) {
        for(int j = 0; j < k; ++j ) {
            cout << result[i][j] << " ";
        }
        cout << endl;
    }
}
