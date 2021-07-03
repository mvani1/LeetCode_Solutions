import threading,time
class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.lock = threading.Semaphore(capacity)
        self.q = deque()
        

    def enqueue(self, element: int) -> None:
        with self.lock:
            self.q.append(element)

    def dequeue(self) -> int:
        while not self.q:
            time.sleep(0.1)
        return self.q.popleft()

    def size(self) -> int:
        return len(self.q) # self.size