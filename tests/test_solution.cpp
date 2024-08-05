4. 테스트 케이스
```cpp
int main() {
    DynamicArray arr1;
    arr1.addElement(10);
    arr1.addElement(20);
    arr1.removeLastElement();
    arr1.printArray(); // 출력: 10
    
    DynamicArray arr2;
    for (int i = 0; i < 5; i++) {
        arr2.addElement(i);
    }
    arr2.removeLastElement();
    arr2.printArray(); // 출력: 0 1 2 3
    return 0;
}
```