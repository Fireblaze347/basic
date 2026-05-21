#include <iostream>
#include <cstdlib>
#include <ctime>

int main()
{
    srand(unsigned(time(NULL)));
    int randomNumber = rand() % 101;
    int guesses = 0;
    while (true){


    std::cout << "Guess a number from 1 - 100\n";
    int x;
    std::cin >> x;

 
    if (x == randomNumber)
    {
        std::cout << "Congrats! you guessed right\n";
        break;
    }
    else if (x > randomNumber)
    {
        std::cout << "Too high\n";
    }
    else
    {
        std::cout << "Too low\n";
    }
    guesses++;
    }
    std::cout << "You took " << guesses << " guesses\n";
    return 0;
}

