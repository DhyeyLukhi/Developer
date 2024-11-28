#include <iostream>
using namespace std;

template<typename T>
using InputFunction = void(*)(T&);

template<typename T>
void Input(T& input) {
    cin >> input;
}

int main() {
    InputFunction<int> intInput = Input<int>;
    InputFunction<double> doubleInput = Input<double>;
    InputFunction<string> stringInput = Input<string>;

    int intValue;
    double doubleValue;
    string stringValue;

    cout << "Enter an integer: ";
    intInput(intValue);

    cout << "Enter a double: ";
    doubleInput(doubleValue);

    cout << "Enter a string: ";
    stringInput(stringValue);

    cout << "You entered: " << intValue << " " << doubleValue << " " << stringValue << endl;

    return 0;
}
