#include<iostream>
using namespace std;
class A{
    int a;
    public:
        A & setData(int a){
            this->a = a;
            return *this;
        }
        
        // void setData(int a){
        //     this->a = a;
        // }


        void getData(){
            cout<<"The value of a is "<<a<<endl;
        }
};

int main(){
    A a;
    a.setData(4).getData();
    // a.setData(4).getData()
    a.getData();
    return 0;
}
