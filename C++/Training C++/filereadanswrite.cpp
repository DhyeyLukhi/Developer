#include<iostream>
#include<fstream>


// These are some useful classes for working with files in C++

// 1. fstreambase
// 2. ifstream --> derived from fstreambase
// 3. ofstream --> derived from fstreambase

using namespace std;

int main(){
    string st = "Dhyey ";
    // Opening files using constructor and writing it
    ofstream out("dhyey.txt"); // Write operation
    out<<st;

    // Here you can give any name after "ofstream" and "ifstream".
    // But giving name with in and out make program readable for you and others.

    string st2;
    // Opening files using constructor and reading it
    ifstream in("dhyey2.txt"); // Read operation
    // in>>st2;
    getline(in, st2);  
    cout<<st2;

    return 0;
}
