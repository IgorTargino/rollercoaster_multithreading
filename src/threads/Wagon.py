from threading import Event, Semaphore, Thread, Lock
from utils.ActionsPassenger import ActionsPassenger
import time


class Wagon(Thread):

    wagonWorkingEvent = Event()

    def __init__(self, travel_time, max_capacity, mutex, semaphore_wagon, queue):
        Thread.__init__(self)
        self.travel_time: int = travel_time
        self.max_capacity: int = max_capacity

        self.state: str = "BOARDING"
        self.seats: int = max_capacity
        self.current_passengers: list = []
        self.queue: list = queue

        self.mutex: Lock = mutex
        self.semaphore_wagon: Semaphore = semaphore_wagon

        print("Thread vagão iniciada")
        self.start()

    def run(self):
        while True:
            self.semaphore_wagon.acquire()
            
            if(self.state == "WALKING"):
                self.start_roller_coaster()

    def start_roller_coaster(self):
        print("Iniciando montanha russa")

        self.mutex.acquire()
        ActionsPassenger.action_queue("sleep", self.queue)
        ActionsPassenger.action_current_passenger(
            "wakeUp", self.current_passengers)
        self.mutex.release()

        print("Percorrendo montanha...")
        time.sleep(self.travel_time)

        self.mutex.acquire()
        ActionsPassenger.action_queue("wakeUp", self.queue)
        self.mutex.release()
