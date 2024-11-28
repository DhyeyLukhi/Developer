#include<iostream>
#include<list>
 
using namespace std;
 
void display(list<int> &lst){
    list<int> :: iterator it;
    for (it = lst.begin(); it != lst.end(); it++)
    {
        cout<<*it<<" ";
    }
    cout<<endl;
    
}
 
int main(){
    
    list<int> list1;  //empty list of 0 length
    list<int> list2(3);  //empty list of length 3
    list<int> :: iterator it = list2.begin();  // making an iterator for the list 2
    *it = 45;
    it++;
    *it = 6;
    it++;
    *it = 9;
    it++;
 
    display(list2);
    list1.pop_back();  // deleting the last element of the list 1
    display(list1);
    list1.pop_front();  // deleting the first element of the list 1
    display(list1);
 
    list1.push_back(5);   // adding the element to the list 1
    list1.push_back(7);   // adding the element to the list 1
    list1.push_back(1);   // adding the element to the list 1
    list1.push_back(9);   // adding the element to the list 1
    list1.push_back(12);  // adding the element to the list 1

    list1.remove(9);  // removing all the 9 in the list 1
    display(list1);

    display(list1);
    list1.sort(); // sorting the list 1
    display(list1);
 
    display(list1);
 
    return 0;
}
