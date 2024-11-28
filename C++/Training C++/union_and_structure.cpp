#include <iostream>

using namespace std;

struct company{
    int employee;
    char namechar;
    float annualincome;
};

// typedef struct company{
//     int employee;
//     char namechar;
//     float annualincome;
// }cmp ;                     // By using typedef now you can access this structure company as cmp   Ex. cmp Dhyey; then initialize the value of variable

union asyourwish{  //In the union memory is shared between the datatypes so we can use only one datatype at one time
//here if we think that int, char, float are taking 4, 1, 4 bytes so union will provide only 4 bytes between these three datatypes insted of 9
    int val1;
    char val2;
    float val3;
};

int main(){
    enum Time {morning, evening, nighttime};
    cout<<"The value is printed using enum "<<morning<<endl;
    cout<<"The value is printed using enum "<<evening<<endl;
    cout<<"The value is printed using enum "<<nighttime<<endl;
    Time nine = morning;
    cout<<"The value is printed using enum "<<nine<<endl;
    struct company first;
    first.employee = 20000;
    first.namechar = 'a';
    first.annualincome = 330000000;
    cout<<"Total number of Employees in the Company "<<first.employee<<endl;
    cout<<"First charatce of the name of the Company is "<<first.namechar<<endl;
    cout<<"Annnual income of the Company is "<<first.annualincome<<endl;
    union asyourwish thing1;
    thing1.val1 = 34342;
    thing1.val2 = 'w';
    cout<<"The Value of Value 1 is "<<thing1.val1<<endl;
    thing1.val3 = 34532.343;
    cout<<"The Value of Value 1 is now "<<thing1.val1<<endl;
    
return 0;
}