#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int i = 0;
    int sum = 0;
    
    while (cin >> i) {
        sum += i;
    }
    
    cout << sum << endl;
    
    return 0;
}
