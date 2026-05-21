#include <stdio.h>
#include <iostream>

long long factorial (long number);

int main()
{   
    long answer;
    std::cout << "Factorial of? ";
    std::cin >> answer;
    std::cout << factorial(answer) << std::endl;
    return 0;

}

long long factorial(long number)
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