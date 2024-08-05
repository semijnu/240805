2. 문제 코드
아래는 프로그램의 대략적인 구조를 보여주는 기본 코드입니다.
```cpp
#include <iostream>
using namespace std;

class DynamicArray {
    int *arr; // 배열의 메모리를 가리키는 포인터
    int size; // 현재 배열의 크기
public:
    DynamicArray(int initialSize = 1); // 배열을 초기화하는 생성자
    ~DynamicArray(); // 배열의 메모리를 해제하는 소멸자
    void addElement(int element); // 원소를 추가하는 메서드
    void removeLastElement(); // 마지막 원소를 제거하는 메서드
    void printArray(); // 배열의 모든 원소를 출력하는 메서드
};

int main() {
    // 여기에 코드를 작성하세요.
}
```