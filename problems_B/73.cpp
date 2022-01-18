#include <iostream>
using namespace std;

int main(){
    int a, b, x;
    int seg[] = {6, 2, 5, 5, 4, 5, 6, 3, 7, 6};
    cin >> a >> b;
    int res = 0;

    for(int i = a; i < b + 1; i++){
        x = i;
        while (x){
            res += seg[x % 10];
            x /= 10;
        }
    }
    cout << res << endl;
}