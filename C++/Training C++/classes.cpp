#include <iostream>

using namespace std;

class Myclass {
    private:
        int a, b, c;
    public:
        int d, e, f;

        void gets(int e, int f);
        void printdata(int a, int b, int c)
        {
            cout<<"The value of a is "<<a<<endl;
            cout<<"The value of b is "<<b<<endl;
            cout<<"The value of c is "<<c<<endl;
            cout<<"The value of d is "<<d<<endl;
            cout<<"The value of e is "<<e<<endl;
            cout<<"The value of f is "<<f<<endl;
        }
};

void Myclass :: gets(int e, int f){
        a = e;
        b = f;
}

int main(){
    Myclass dhyey;
    dhyey.d = 95;
    dhyey.e = 9;
    dhyey.f = 55;
    dhyey.gets(dhyey.d, dhyey.e);
    dhyey.printdata(dhyey.d, dhyey.e, dhyey.f);


return 0;
}