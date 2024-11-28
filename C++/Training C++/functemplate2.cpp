#include <iostream>
using namespace std;

template<class T1, class T2>
float funcAverage(T1 a, T2 b){
    float avg= (a+b)/2.0; 
    return avg;
}

template <class T>
void swapp(T &a, T &b)
{
    T temp = a;
    a = b;
    b = temp;

}

int main(){
    float a;
    a = funcAverage(5,2);
    printf("The average of these numbers is %0.3f\n",a);
    int x = 9, y = 10;
    swapp(x, y);
    cout<<"The value of X is "<<x<<endl<<"The value of Y is "<<y<<endl;
    return 0;
}
