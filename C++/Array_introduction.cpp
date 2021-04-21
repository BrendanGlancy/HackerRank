#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int N;
    cin >> N;
    int arr[N];
    // Read in the array
    for (int i = 0; i < N; i++)
    {
        cin >> arr[N];
    }
    // print out array in reverse
    for (int i = N-1; i >= 0; i--)
    {
        cout << arr[i] << " ";
    }
    return 0;
}

