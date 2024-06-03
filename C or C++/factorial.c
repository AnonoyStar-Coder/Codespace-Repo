#include<stdio.h>

int factorial(int a);

int main() 
{
    int n, fact;

    printf("\nEnter number to find factorial: ");
   
    scanf("%d", &n);

    fact = factorial(n);

    printf("\nFactorial of number is %d", fact);

    return 0;
}

int factorial(int a) 
{
    if (a == 0 || a == 1) 
    {
        return 1;
    } 
    else 
    {
        return a * factorial(a - 1);
    }
}