 
//include libraries
#include <iostream>
#include <string>
#include <fstream>
//cout and cin library
using namespace std;
class priorityQueue
{
private:
    int *heap;
    int heapSize;
    int maxSize;
    void heapRebuild(int root);
public:
    priorityQueue(int size = 100);
    ~priorityQueue();
    bool isEmpty() const;
    bool enqueue(const int& newItem);
    bool dequeue(int& queueFront);
    bool peek(int& queueFront) const;
    void print();
};

bool priorityQueue::isEmpty() const
{
    return heapSize == 0;
}

bool priorityQueue::enqueue(const int& newItem)
{
    if (heapSize == maxSize)
        return false;
    int newNode = heapSize;
    heapSize++;
    while (newNode > 0 && newItem > heap[(newNode - 1) / 2])
    {
        heap[newNode] = heap[(newNode - 1) / 2];
        newNode = (newNode - 1) / 2;
    }
    heap[newNode] = newItem;
    return true;
}

bool priorityQueue::dequeue(int& queueFront)
{
    if (isEmpty())
        return false;
    queueFront = heap[0];
    heapSize--;
    heap[0] = heap[heapSize];
    heapRebuild(0);
    return true;
}

bool priorityQueue::peek(int& queueFront) const
{
    if (isEmpty())
        return false;
    queueFront = heap[0];
    return true;
}

void priorityQueue::heapRebuild(int root)
{
    int child = 2 * root + 1;
    if (child < heapSize)
    {
        int rightChild = child + 1;
        if (rightChild < heapSize && heap[rightChild] > heap[child])
            child = rightChild;
        if (heap[root] < heap[child])
        {
            int temp = heap[root];
            heap[root] = heap[child];
            heap[child] = temp;
            heapRebuild(child);
        }
    }
}

priorityQueue::priorityQueue(int size)
{
    maxSize = size;
    heapSize = 0;
    heap = new int[maxSize];
}

priorityQueue::~priorityQueue()
{
    delete[] heap;
}

void priorityQueue::print()
{
    for (int i = 0; i < heapSize; i++)
        cout << heap[i] << " ";
    cout << endl;
}



int main() {
  
    //a priority queue of type string
    priorityQueue queue;
    //test enqueue
    queue.enqueue(1);
    queue.enqueue(2);
    queue.enqueue(3);
    queue.enqueue(4);

    //print the queue
    queue.print();


    return 0;
}
