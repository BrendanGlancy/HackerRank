#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    // Complete the code.
    int x;
    long y;
    char a;
    float z;
    double b;
    cin >> x >> y >> a >> z >> b;
    cout << x << "\n" << y << "\n" << a << "\n";
    printf("%.3f\n", z); 
    printf("%.9lf", b);
    return 0;
}
