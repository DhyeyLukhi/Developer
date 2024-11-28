#include<iostream>
#include<vector>
using namespace std;


void display(vector<int> &v){
    for (int i = 0; i < v.size(); i++)
    {
        cout<<v[i]<<" ";
    }
    cout<<endl;
}


int main(){ 
    vector<int> vec1;
    int element, size;
    cout<<"Enter the size of your vector"<<endl;
    cin>>size;
    for (int i = 0; i < size; i++)
    {
        cout<<"Enter an element to add to this vector: ";
        cin>>element;
        vec1.push_back(element);
    }

    display(vec1);
    // To create a iterator here is the code-->:  vector<datatype> :: iterator iteratorname = vectorname.begin()
    // In the code ".begin" says that the iterator object is pointing to the statring element of the vector 
    vector<int> :: iterator iter = vec1.begin();
    vec1.insert(iter,566);
    display(vec1);
    display(vec1);    
    return 0;
}

    // display(vec1);
    // vec1.pop_back();
    // display(vec1);
    // vector<int> vec1;      //zero length integer vector
    // vector<char> vec2(4);  //4-element character vector
    // vector<char> vec3(vec2);//4-element character vector from vec2
    // vector<int> vec4(6,3); //6-element vector of 3s