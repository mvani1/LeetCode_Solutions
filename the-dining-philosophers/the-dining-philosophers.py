from threading import Lock
class DiningPhilosophers:
    def __init__(self):
        self.lock = [Lock() for i in range(5)]
    # call the functions directly to execute, for example, eat()
    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        if philosopher != 0:
            first , second = philosopher, (1+philosopher)%5
        else:
            second , first = philosopher, (1+philosopher)%5            
        with self.lock[first]:
            with self.lock[second]:
                pickLeftFork()
                pickRightFork()
                eat()
                putLeftFork()
                putRightFork()