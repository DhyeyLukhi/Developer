#include <iostream>
#include <cmath>
using namespace std;

int a1, a2, b1, b2;

class Maths
{
    int a, b;
    friend float dist(int, int, int, int);

public:
    float dist(int, int, int, int);
    void display(float d)
    {
        cout << "The Distance between (" << a1 << ", " << b1 << ") and (" << a2 << ", " << b2 << ") is " << d << endl;
    }
};

float Maths ::dist(int x1, int y1, int x2, int y2)
{
    a = (x1 - x2) * (x1 - x2);
    b = (y1 - y2) * (y1 - y2);
    if (a >= b)
    {
        float distan = sqrt(a - b);
        return distan;
    }
    else
    {
        float distan = sqrt(b - a);
        return distan;
    }
}

int main()
{
    Maths a;
    cout << "Enter the x1: ";
    cin >> a1;
    cout << "Enter the y1: ";
    cin >> b1;
    cout << "Enter the x2: ";
    cin >> a2;
    cout << "Enter the y2: ";
    cin >> b2;
    float res = a.dist(a1, b1, a2, b2);
    a.display(res);
    return 0;
}