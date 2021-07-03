import threading
class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.enq = threading.Semaphore(capacity)
        self.deq = threading.Semaphore(0)
        self.queue = deque()

    def enqueue(self, element: int) -> None:
        self.enq.acquire()
        self.queue.append(element)
        self.deq.release()

    def dequeue(self) -> int:
        self.deq.acquire()
        ele = self.queue.popleft()
        self.enq.release()
        return ele
    def size(self) -> int:
        return len(self.queue)