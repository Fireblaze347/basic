#include <stdio.h>
#include <iostream>

int factorial (int number);

int main()
{
    std::cout << factorial(10);
    return 0;

}

long long factorial(long long number)
{
    if (number == 1)
    {
        return number;
    }
    else
    {
        return number * factorial(number-1);
    }
}