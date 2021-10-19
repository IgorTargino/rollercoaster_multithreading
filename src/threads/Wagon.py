from threading import Event, Thread, Semaphore
from utils.ActionsPassenger import actionQueue, actionCurrentPassenger
import time


BOARDING = 0
DISEMBARKING = 1
WALKING = 2


class Wagon(Thread):

    wagonWorkingEvent = Event()

    def __init__(self, travelTime, maxCapacity, semaphoreWagon, mutex):
        Thread.__init__(self)
        self.travelTime = travelTime
        self.maxCapacity = maxCapacity
        self.seats = maxCapacity
        self.state = BOARDING
        self.currentPassengers = []

        self.semaphoreWagon = semaphoreWagon
        self.mutex = mutex

    def run(self):
        while True:
            print("Thread vagão iniciada")
            self.sleep()
            self.startRollerCoaster()

    def startRollerCoaster(self):
        print("Iniciando montanha russa")
        if(~self.available()):
            self.wakeUp()

        self.mutex.acquire()
        actionQueue("sleep")
        actionCurrentPassenger("wakeUp")
        self.mutex.release()

        print("Percorrendo montanha...")
        time.sleep(self.travelTime)

        self.sleep()

        self.mutex.acquire()
        actionQueue("wakeUp")
        self.mutex.release()

    def available(self):
        return self.wagonWorkingEvent.isSet()

    def sleep(self):
        print("Thread vagao dormindo")
        self.wagonWorkingEvent.wait()

    def wakeUp(self):
        print("Thread vagao acordada")
        self.wagonWorkingEvent.set()
