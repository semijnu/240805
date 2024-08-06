```cpp
#include <iostream>

int main() {
    int num;
    std::cin >> num;

    if (num > 0)
    {
        std::cout << "Positive number";
    } 
    else if (num < 0)
    {
        std::cout << "Negative number";
    }
    else
    {
        std::cout << "Zero";
    }
    
    return 0;
}
```

4. 테스트 케이스