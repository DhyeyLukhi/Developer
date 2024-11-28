#include<iostream>
using namespace std;


// If a member of Base Class is Private but you want to inherit it in the Derived Class, Use Protected

class Base{
    protected:
        int a; 
    private:
        int b;

};

class Derived: protected Base{
   
};

int main(){
    Base b;
    Derived d;
    // cout<<d.a; // Will not work since a is protected in both base as well as derived class
    return 0;
}



// Here this graph shows behaviour of members when they are inherited

/*

                       |    Public Derivation    |    Private Derivation    |    Protected Derivation
                       |                         |                          |
1. Private Members     |      Not Inherited      |     Not Inherited        |      Not Inherited
                       |                         |                          |
2. Protected Members   |        Protected        |        Private           |        Protected
                       |                         |                          |
3. Public Members      |         Public          |        Private           |        Protected              



Tips: 

1. Private Members are not Inheritable
2. Public Members' Inheritence = visibility mode of Derived Class
3. Protected Members are Irotected in Public and Protected Derivation and they becomes Private in Private Derivation

*/