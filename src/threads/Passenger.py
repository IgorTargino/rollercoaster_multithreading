from threading import Thread, Semaphore, Event
import time


class Passenger(Thread):

    passengerEvent = Event()

    def __init__(self, id, boardingTime, disembarkationTime):

        Thread.__init__(self)

        self.id = id
        self.boardingTime = boardingTime
        self.disembarkationTime = disembarkationTime

        mutex.acquire()
        currentId += 1
        mutex.release()

    def run(self):
        print("Thread passageiro {} iniciada!".format(self.id))
        self.wakeUp()

    def toBoard(self):
        print("Passageiro {} embarcando".format(self.id))
        if(len(currentPassengers) < capacity):
            mutex.acquire()
            del queue[0]
            currentPassengers.append(self)
            mutex.release()
        time.sleep(self.boardingTime)

    def land(self):
        print("Passageiro {} desembarcando".format(self.id))
        mutex.acquire()
        del currentPassengers[0]
        queue.apeend(self)
        mutex.release()
        time.sleep(self.disembarkationTime)

    def enjoyTheLandscape(self):
        mutex.acquire()
        actionCurrentPassenger("wakeUp")
        mutex.release()

    def available(self):
        return self.passengerEvent.isSet()

    def sleep(self):
        print("Thread passageiro {} dormindo".format(self.id))
        self.passengerEvent.wait()

    def wakeUp(self):
        print("Thread passageiro {} acordada".format(self.id))
        self.passengerEvent.set()
