#include <stdio.h>

int find_gcd( int, int);

int main()
{
    int n1, n2, gcd;
    printf("N1: ");
    scanf("%d", &n1);
    printf("N2: ");
    scanf("%d", &n2);
    gcd = find_gcd(n1, n2);
    printf("Value of gcd %d", gcd);
    return 0;

}

int find_gcd(int m, int n)
{
    int gcdval;
    if (n > m)
    {
        gcdval = find_gcd(n, m);
    }
    else if (n == 0)
    {
        gcdval = m;
    }
    else
    {
        gcdval = find_gcd(n ,m%n);
    }

    return(gcdval);
    
    
    
}
