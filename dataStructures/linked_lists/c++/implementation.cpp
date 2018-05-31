#include<iostream>
#include<string>

template<class T>
class Node {  

    private:
    Node<T> *tail() {
        Node<T> *cur = this;
        while(cur->Next) {
            cur = cur->Next;
        }
        return cur;
    }
    public:
    T Data;
    Node<T>* Next;

    Node<T>(T value) {
        Data = value;
        Next = NULL;
    }
    
    T peek() const {
        return tail()->Data;
    }
    
    int length() const {
        Node<T> const *cur = this;
        int counter = 0;
        while(cur) {
            counter ++;
            cur = cur->Next;
        }
        return counter;
    }
    
    void push(T value) {
        tail()->Next = new Node<T>(value);
    }

    T pop() {
        Node<T> *cur = this;
        T last;
        while(cur->Next) {
            if(cur->Next->Next) {    
                cur = cur->Next;
            } else {
                last = cur->Next->Data;
                cur->Next = NULL;
            }
        }

        return last;
    }

};

int main(){
    std::string s = "";
    Node<int> a = Node<int>(4);
    a.push(3);
    std::cout << a.length();
    a.push(3);
    std::cout << a.length();
    a.pop();
    std::cout << a.length();
    std::cin >> s;
}
