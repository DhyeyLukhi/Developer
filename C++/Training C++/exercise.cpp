#include <iostream>
#include<cmath>
using namespace std;

class Simplecalculator{
    float num1, num2;
    public:
        Simplecalculator(){
            cout<<"Enter the Number 1: ";
            cin>>num1;
            cout<<"Enter the Number 2: ";
            cin>>num2;
        }
        void Result();
        
};

void Simplecalculator :: Result (){
    cout<<"The Addition of "<<num1<<" and "<<num2<<" is "<<num1+num2<<endl;
    cout<<"The Substraction of "<<num1<<" and "<<num2<<" is "<<num1-num2<<endl;
    cout<<"The Multiplication of "<<num1<<" and "<<num2<<" is "<<num1*num2<<endl;
    cout<<"The Division of "<<num1<<" and "<<num2<<" is "<<num1/num2<<endl;
}



class ScientifictCalculator{
    float num1, num2;
    public:
        int choice;
        ScientifictCalculator(){
            
            cout<<"Enter 1. Squareroot"<<endl<<
                  "      2. Loge and log10"<<endl<<
                  "      3. Sine Value"<<endl<<
                  "      4. Cosine value"<<endl;
            cin>>choice;
        }
        void DisplayResult();
};


void ScientifictCalculator :: DisplayResult(){
    switch (choice)
    {
    case 1:
        cout<<"Enter the Number: ";
        cin>>num1;
        cout<<"The Squareroot of "<<num1<<" is "<<sqrt(num1)<<endl;
        break;
    case 2:
        cout<<"Enter the Number: ";
        cin>>num1;
        cout<<"Log with base e : "<<log(num1)<<endl;
        cout<<"Log with base 10 : "<<log10(num1)<<endl;
        break;
    case 3:
        cout<<"Enter the Number: ";
        cin>>num1;
        cout<<"Sine("<<num1<<") = "<<sin(num1)<<endl;
        break;
    case 4:
        cout<<"Enter the Number: ";
        cin>>num1;
        cout<<"Cos("<<num1<<") = "<<cos(num1)<<endl;
        break;
    default:
        break;
    }
}


int main(){
    // Here is Simple Calculator 
    // Simplecalculator dhyey1;
    // dhyey1.Result();

    // Here is a scientific Calculator
    ScientifictCalculator dhyey2;
    dhyey2.DisplayResult();

    
return 0;
}