import threading
import time

queue = []
currentPassengers = []

global capacity
currentId = 0

mutex = threading.Lock()
wagonWorkingEvent = threading.Event()
passengerEvent = threading.Event()


class wagon (threading.Thread):

    def __init__(self, travelTime, maxCapacity):
        threading.Thread.__init__(self)
        self.travelTime = travelTime
        self.maxCapacity = maxCapacity

    def run(self):
        print("Thread vagão iniciada!")
        self.sleep()

    def startRollerCoaster(self):
        print("Iniciando montanha russa")

        actionQueue("sleep")
        actionCurrentPassenger("wakeUp")

        print("Percorrendo montanha...")
        time.sleep(self.travelTime)

    def pauseRollerCoaster(self):
        print("Parando montanha russa")

        for passenger in currentPassengers:
            passenger.land()

    def available(self):
        return self.wagonWorkingEvent.isSet()

    def sleep(self):
        print("Thread vagao dormindo")
        self.wagonWorkingEvent.wait()

    def wakeUp(self):
        print("Thread vagao acordada")
        self.wagonWorkingEvent.set()


class passenger (threading.Thread):

    def __init__(self, boardingTime, disembarkationTime):

        threading.Thread.__init__(self)
        global currentId

        self.id = currentId
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

    def available(self):
        return self.passengerEvent.isSet()

    def sleep(self):
        print("Thread passageiro {} dormindo".format(self.id))
        self.passengerEvent.wait()

    def wakeUp(self):
        print("Thread passageiro {} acordada".format(self.id))
        self.passengerEvent.set()


class rollerCoaster(threading.Thread):

    def __init__(self, maxCapacity, travelTime):
        threading.Thread.__init__(self)

        mutex.acquire()
        global capacity
        capacity = maxCapacity
        mutex.release()

        vagao = wagon(capacity, travelTime)
        vagao.start()
        vagao.join()

        self.vagao = vagao
        print("Thread Montanha russa iniciada!")

    def run(self):
        while True:
            print(self.vagao.available())


def newPassenger(boardingTime, disembarkationTime):
    print("Inserindo novo passageiro")
    currentPassenger = passenger(boardingTime, disembarkationTime)
    queue.append(currentPassenger)
    currentPassenger.start()
    currentPassenger.join()


def newWagon(mCapacity, travelTime):
    mutex.acquire()
    global capacity
    capacity = mCapacity
    mutex.release()
    vagao = wagon(capacity, travelTime)
    vagao.start()


def actionQueue(method):
    if(method == "sleep"):
        for passenger in queue:
            passenger.sleep()
    elif(method == "wakeUp"):
        for passenger in queue:
            passenger.wakeUp()


def actionCurrentPassenger(method):
    if(method == "sleep"):
        for passenger in currentPassengers:
            passenger.sleep()
    elif(method == "wakeUp"):
        for passenger in currentPassengers:
            passenger.wakeUp()


def main():
    newWagon(3, 3)
    newPassenger(4, 4)
    newPassenger(5, 5)
    newPassenger(4, 4)


if __name__ == '__main__':
    main()
