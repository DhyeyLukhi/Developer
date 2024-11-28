#include <iostream>

using namespace std;

int main(){
    int a=3;
    int *b = &a;
    cout<<"The value of B using B is "<<b<<endl;
    cout<<"The Address of A using A is "<<&a<<endl;
    cout<<"The Address of B using B is "<<&b<<endl;
    cout<<"The value of A using B is "<<*b<<endl;

    int ** c = &b;
    cout<<"The Address of B using C "<<c<<endl;

    // i have to keep updating the number of '*' to store pointer to pointer variable as many in chain

return 0;
}