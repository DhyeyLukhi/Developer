#include <iostream>
#include <fstream>
#include <string>
 
using namespace std;
 
int main()
{

     // declaring an object of the type ofstream
    ofstream out;
 
    //connecting the object out to the text file using the member function open()
    out.open("dhyey.txt");
 
    //writing to the file
    out <<"This is me\n";
    out <<"This is also me\n";
    out <<"This is me also\n";
    out <<"This is me again\n";
    //closing the file connection
    out.close();

    // declaring an object of the type ifstream
    ifstream in;
    //declaring string variable st
    string st;
    //opening the text file into in
    in.open("dhyey.txt");
 
    // giving output the string lines by storing in st until the file reaches the end of it
    while (in.eof()==0) 
    {
        // using getline to fill the whole line in st
        getline(in,st);
        cout<<st<<endl;
    }
    return 0;
}
