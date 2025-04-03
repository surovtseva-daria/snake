#include <iostream>
using namespace std;

class Stack {
public:
    // Стек для хранения элементов
    int arr[100];
    int top = -1;

    // Операция push
    void push(int x) {
        arr[++top] = x;
    }

    // Операция pop
    int pop() {
        if (top == -1) {
            throw runtime_error("Stack is empty");
        }
        return arr[top--];
    }

    // Операция проверки на пустоту
    bool isEmpty() {
        return top == -1;
    }
};

class Queue {
private:
    Stack stack1, stack2;

    // Перемещаем все элементы из stack1 в stack2
    void transferElements() {
        while (!stack1.isEmpty()) {
            stack2.push(stack1.pop());
        }
    }

public:
    // Операция enqueue (добавление в очередь)
    void enqueue(int x) {
        stack1.push(x);
    }

    // Операция dequeue (удаление из очереди)
    int dequeue() {
        if (stack2.isEmpty()) {
            if (stack1.isEmpty()) {
                throw runtime_error("Queue is empty");
            }
            // Переносим элементы из stack1 в stack2
            transferElements();
        }
        return stack2.pop();
    }

    // Операция проверки, пуста ли очередь
    bool isEmpty() {
        return stack1.isEmpty() && stack2.isEmpty();
    }
};

int main() {
    Queue q;

    // Пример использования очереди
    q.enqueue(1);
    q.enqueue(2);
    q.enqueue(3);

    cout << q.dequeue() << endl; // Ожидаем 1
    cout << q.dequeue() << endl; // Ожидаем 2

    q.enqueue(4);

    cout << q.dequeue() << endl; // Ожидаем 3
    cout << q.dequeue() << endl; // Ожидаем 4

    return 0;
}