#include <iostream>
#include <iomanip>

int main() {

    double students = 29;
    
    students/=13;

    std::cout << std::fixed;
    std::cout << std::setprecision(2);
    std:: cout << students;

    return 0;
}