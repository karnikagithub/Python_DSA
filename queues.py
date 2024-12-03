from collections import deque
import threading
import time


class Queue:
    def __init__(self):
        self.container = deque()

    def enqueue(self,value):
        self.container.appendleft(value)
    
    def dequeue(self):
        if len(self.container)==0:
            print("Queue is empty")
            return
         
        return self.container.pop()
    
    def is_empty(self):
        return len(self.container) == 0
    
    def size(self):
        return len(self.container)
    

pq = Queue()

pq.enqueue({
    'comp':'IBM',
    'timestamp':'11:01',
    'price':'1000'
})
pq.enqueue({
    'comp':'IBM',
    'timestamp':'11:02',
    'price':'1001'
})
pq.enqueue({
    'comp':'IBM',
    'timestamp':'11:03',
    'price':'1003'
})
pq.enqueue({
    'comp':'IBM',
    'timestamp':'11:04',
    'price':'1005'
})

# print(pq.size())
# print(pq.container)
# print(pq.dequeue())

food_order_queue = Queue()

def place_orders(orders):
    for order in orders:
        print("Placing order for:",order)
        food_order_queue.enqueue(order)
        time.sleep(0.5)


def serve_orders():
    time.sleep(1)
    while True:
        order = food_order_queue.dequeue()
        print("Now serving: ",order)
        time.sleep(2)

if __name__ == '__main__':
    orders = ['pizza','samosa','pasta','biryani','burger']
    t1 = threading.Thread(target=place_orders, args=(orders,))
    t2 = threading.Thread(target=serve_orders)

    t1.start()
    t2.start()