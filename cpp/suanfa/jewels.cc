#include <iostream>
#include <string>
using std::cout;
using std::cin;
using std::string;

int jewels(string J, string S) {
    int count = 0;
    for(int i=0; i<S.size();++i) {
        for(int j=0; j < J.size(); ++j){
            if(J[j] == S[i])
                ++count;
            }
        }
    return count;
}
int jewels2(string J, string S) 
{
    int amount[52] = { 0 };
    int ans = 0;
    for (int i = 0; i < S.size(); i++)
    {
        if (S[i] >= 'a')
            amount[S[i] - 'a']++;
        else
            amount[S[i] - 'A' + 26]++;
    }
    for (int i = 0; i < J.size(); i++)
    {
        if (J[i] >= 'a')
            ans += amount[J[i] - 'a'];
        else
            ans += amount[J[i] - 'A' + 26];
    }
    return ans;
}

int main() {
    int a = 0;
    //int answer = 3;
    int answer = 0;
    string s1 = "z";
    string s2 = "ZZ";
    //string s1 = "aA";
    //string s2 = "aAAbbbb";
    a = jewels2(s1, s2);
    if (answer == a) {
        printf("you are right\n");
    }
}
