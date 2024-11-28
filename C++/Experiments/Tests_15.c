#include <stdio.h>
enum menu {Exit, Add, Subtract, Multiply, Divide};
int main()
{
    int choice, num1, num2, result;
    printf("Welcome to the calculator program\n");
    printf("Please choose an option from the menu:\n");
    printf("0. Exit\n");
    printf("1. Add\n");
    printf("2. Subtract\n");
    printf("3. Multiply\n");
    printf("4. Divide\n");
    scanf("%d", &choice);
    while (choice != Exit)
    {
        printf("Enter two numbers:\n");
        scanf("%d %d", &num1, &num2);
        switch (choice)
        {
        case Add:
            result = num1 + num2;
            printf("The sum of %d and %d is %d\n", num1, num2, result);
            break;
        case Subtract:
            result = num1 - num2;
            printf("The difference of %d and %d is %d\n", num1, num2, result);
            break;
        case Multiply:
            result = num1 * num2;
            printf("The product of %d and %d is %d\n", num1, num2, result);
            break;
        case Divide:
            if (num2 == 0)
            {
                printf("Cannot divide by zero\n");
            }
            else
            {
                result = num1 / num2;
                printf("The quotient of %d and %d is %d\n", num1, num2, result);
            }
            break;
        default:
            printf("Invalid choice\n");
            break;
        }
        
        printf("Please choose another option from the menu:\n");
        printf("0. Exit\n");
        printf("1. Add\n");
        printf("2. Subtract\n");
        printf("3. Multiply\n");
        printf("4. Divide\n");
        scanf("%d", &choice);
    }
    printf("Thank you for using the calculator program\n");
    return 0;
}
