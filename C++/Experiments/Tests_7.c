#include <stdio.h>

int main() {

    int spot;
    char ch;
    char str1[100];

    printf("Enter the string: ");
    scanf("%s", str1);
    
    // Add a space before %c to consume the newline character

    for(int i = 0; i < 100; i++) {
        if (ch == str1[i]) {
            spot = i;
            printf("The character is spotted in the string at %d\n", spot+1);
            break;
        }
    }

    return 0;
}
