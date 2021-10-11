import threading
import time

currentId = 0
queue = []

mutex = threading.Lock()


class wagon (threading.Thread):

    wagonWorkingEvent = threading.Event()

    def __init__(self, travelTime, maxCapacity):
        threading.Thread.__init__(self)
        self.travelTime = travelTime
        self.maxCapacity = maxCapacity

    def run(self):
        print("Thread vagão iniciada!")

    def available(self):
        return self.wagonWorkingEvent.isSet()

    def sleep(self):
        self.wagonWorkingEvent.wait()

    def wakeUp(self):
        self.wagonWorkingEvent.set()


class passenger (threading.Thread):

    passengerEvent = threading.Event()

    def __init__(self, boardingTime, disembarkationTime):
        threading.Thread.__init__(self)
        self.id = len(queue) + 1
        self.boardingTime = boardingTime
        self.disembarkationTime = disembarkationTime

    def run(self):
        print("Thread passgeiro {} iniciada!".format(self.id))

    def available(self):
        return self.passengerEvent.isSet()

    def sleep(self):
        self.passengerEvent.wait()

    def wakeUp(self):
        self.passengerEvent.set()


def newPassenger(boardingTime, disembarkationTime):

    currentPassenger = passenger(boardingTime, disembarkationTime)
    queue.append(currentPassenger)
    currentPassenger.start()


def main():
    vagao = wagon(15, 3)
    vagao.start()

    newPassenger(4, 4)
    newPassenger(5, 5)
    newPassenger(6, 6)


if __name__ == '__main__':
    main()
