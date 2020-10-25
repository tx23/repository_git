#include <iostream>
#include <vector>
using namespace std;

//O(1)空间复杂度，O(M*N)时间复杂度
//对一矩阵，若某值为0，设置其行列均为0

void setZeros(vector<vector<int> >& matris) {
    bool row = false, column = false;//第一行标志位

    int matrisRow = matris.size();
    int matrisColumn = matris[0].size();

    for(int i = 0; i < matrisRow; ++i) {
        for(int j = 0; j < matrisColumn; ++j) {
            if(matris[i][j] == 0) {
                if(i == 0)
                    row = true;
                if(j == 0)
                    column = true;
                matris[i][0] = 0;
                matris[0][j] = 0;
            }
        }
    }

    for(int i = 1; i < matrisRow; ++i) {//处理行
        if(matris[i][0] == 0) {
            for(int j = 1; j < matrisColumn; ++j)
                matris[i][j] = 0;
        }
    }

    for(int j = 1; j < matrisColumn; ++j) {//处理列
        if(matris[0][j] == 0) {
            for(int i = 1; i < matrisRow; ++i)
                matris[i][j] = 0;
        }
    }

    //处理首行及首列
    if(row) {
        for(int j = 1; j < matrisColumn; j++)
            matris[0][j] = 0;
    }

    if(column) {
        //for(int i = 1; i< matrisColumn; i++)//数组越界
        for(int i = 1; i< matrisRow; i++)
            matris[i][0] = 0;
    }

}

int main() {

    //设置初始数组
    vector<vector<int> > matris;
    vector<int> v1, v2, v3;
    v1.push_back(0);
    v1.push_back(0);
    v1.push_back(1);
    v1.push_back(1);
    v2.push_back(1);
    v2.push_back(1);
    v2.push_back(0);
    v2.push_back(1);
    v3.push_back(1);
    v3.push_back(1);
    v3.push_back(1);
    v3.push_back(1);
    matris.push_back(v1);
    matris.push_back(v2);
    matris.push_back(v3);
   
    cout << "数组设置前：" << endl;
    for(int i = 0; i < matris.size(); ++i) {
        for(int j = 0; j < matris[0].size(); ++j)
            cout << matris[i][j] << " ";
        cout << endl;   
    }

    setZeros(matris);

    cout << "数组设置后：" << endl;
    for(int i = 0; i < matris.size(); ++i) {
        for(int j = 0; j < matris[0].size(); ++j)
            cout << matris[i][j] << " ";
        cout << endl;   
    }
    return 0;
}
