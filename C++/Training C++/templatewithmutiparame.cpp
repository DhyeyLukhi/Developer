#include <iostream>
using namespace std;

template<class T1, class T2>
class myClass{
    public:
        T1 data1;
        T2 data2;
        myClass(T1 a,T2 b){
            data1 = a;
            data2 = b;
        }
    void display(){
        cout<<this->data1<<" "<<endl<<this->data2;
    }
};

int main()
{
    myClass<int, float> obj(1, 1.8 );
    obj.display();
    return 0;
}

/*
--> You can give datatype to class as your wish using template
--> If we don't use template then we have to make different classes for each datatype or possiblities of datatype
*/