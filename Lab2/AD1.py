class Customer:
    def __init__(self,name,transactionID):
        self.name=name
        self.transactionID=transactionID
    
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()


class Bank:
    def __init__(self):
        self.queue = Queue()
        
    def add_customer(self,name,transactionID):
        self.queue.enqueue(Customer(name,transactionID))
    
    def serve_customer(self):
        print(f"Customer {self.queue.items[0].name} served")
        self.queue.dequeue()
    
    def is_queue_empty(self):
        return self.queue.isEmpty()
    
if __name__ == "__main__":
    exit = False
    bank=Bank()
    while not exit:
        x = input("Enter customer name: ")
        y = input("Enter transaction id: ")
        bank.add_customer(x,y)
        z =int( input("-1 to exit else continue: "))
        if z == -1:
            exit = True
            
    bank.serve_customer
        
    