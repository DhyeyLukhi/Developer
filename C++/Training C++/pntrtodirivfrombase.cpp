#include<iostream>
using namespace std;
class BaseClass{
    public:
        int var_base;
        void display(){
            cout<<"Dispalying Base class variable var_base "<<var_base<<endl;
        }
};

class DerivedClass : public BaseClass{
    public:
            int var_derived;
            void display(){
                cout<<"Dispalying Base class variable var_base "<<var_base<<endl;
                cout<<"Dispalying Derived class variable var_derived "<<var_derived<<endl;
            }
};

int main(){
    BaseClass * base_class_pointer;
    BaseClass obj_base;   // If we create an pointer of base class and point it to te ceriveed class then still...
    DerivedClass obj_derived;   // It can access only the functions of base class because, pointer is from base class
    base_class_pointer = &obj_derived; // Pointing base class pointer to derived class

    base_class_pointer->var_base = 34;
    // base_class_pointer->var_derived= 134; // Will throw an error
    base_class_pointer->display();

    base_class_pointer->var_base = 3400; 
    base_class_pointer->display();

    DerivedClass * derived_class_pointer;
    derived_class_pointer = &obj_derived;
    derived_class_pointer->var_base = 9448;
    derived_class_pointer->var_derived = 98;
    derived_class_pointer->display();

    return 0;
}


// 1. We created a pointer “base_class_pointer” of the data type “Baseclass”.
// 2. Object “obj_base” of the data type “BaseClass” is created.
// 3. Object “obj_derived” of the data type “DerivedClass” is created
// 4. Pointer “base_class_pointer” of the base class is pointing to the object “obj_derived” of the derived class
// 5. By using the pointer “base_class_pointer” of the base class we have set the value of the data member “var_base” by “34”. The main thing to note here is that we cannot set the value of the derived class data member by using the base class pointer otherwise the compiler will throw an error.
// 6. The function “display” is called using a base class pointer. The main thing to note here is that the base class “display” function will run here.
// 7. Again by using the pointer “base_class_pointer” of the base class we have set the value of the data member “var_base” by “3400” which will update the previous value and the function “display” is called.
// 8. We created a pointer “derived_class_pointer” of the data type “DerivedClass”
// 9. Pointer “Derived_class_pointer” of the derived class is pointing to the object “obj_derived” of the derived class
// 10. By using pointer “Derived_class_pointer” of the derived class we have set the value of the data member “var_base” of the base class by “9448”. The main thing to note here is that this will not throw an error because we can set the value of base class data member by using derived class pointer but we cannot set the value of derived class data member by using base class pointer
// 11. By using pointer “Derived_class_pointer” of the derived class we have set the value of the data member “var_derived” of the derived class by “98”.
// 12. The function “display” is called using a derived class pointer. The main thing to note here is that the derived class “display” function will run here
