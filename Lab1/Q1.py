class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop() if self.items else None
    def is_empty(self):
        return not self.items

class StackQueue:
    def __init__(self):
        self.s1=Stack()
        self.s2=Stack()
    def enqueue(self,item):
        self.s1.push(item)
    def dequeue(self):
        if self.s2.is_empty():
            while not self.s1.is_empty():
                self.s2.push(self.s1.pop())
        return self.s2.pop()
                  
        

def main():
    q1=StackQueue()
    q1.enqueue(1)
    q1.enqueue(2)
    q1.enqueue(4)
    q1.enqueue(3)
    print(q1.dequeue(),q1.dequeue(),q1.dequeue(),q1.dequeue(),q1.dequeue())



if __name__ == "__main__":
    main()
