import threading
class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.enq = threading.Semaphore(capacity)
        self.deq = threading.Semaphore(0)
        self.queue = deque()
        self.sizes = 0

    def enqueue(self, element: int) -> None:
        self.enq.acquire()
        self.queue.append(element)
        self.deq.release()
        self.sizes+=1

    def dequeue(self) -> int:
        self.deq.acquire()
        ele = self.queue.popleft()
        self.sizes-=1
        self.enq.release()
        return ele
    def size(self) -> int:
        return self.sizes