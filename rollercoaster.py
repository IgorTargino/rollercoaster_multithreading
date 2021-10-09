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
        while True:
            self.walk()

    def walk(self):

        if(len(queue) == self.maxCapacity):
            self.wakeUp()
            print("Percorrendo montanha...")
            # Colocar fila pra dormir
            time.sleep(self.travelTime)
            # Acordar fila

            print("Parando na estação")
        else:
            self.sleep()

    def available(self):
        # Return true if and only if the internal flag is true.
        return self.wagonWorkingEvent.isSet()

    # barber wait() for an event to occur
    def sleep(self):
        # Block until the internal flag is true. If the internal flag is true on entry, return immediately. Otherwise, block until another thread calls set() to set the flag to true, or until the optional timeout occurs.
        self.wagonWorkingEvent.wait()

    # barber wakes up and event is set()
    def wakeUp(self):
        self.wagonWorkingEvent.set()


class passenger (threading.Thread):

    def __init__(self, id, boardingTime, disembarkationTime):
        threading.Thread.__init__(self)
        self.id = id
        self.boardingTime = boardingTime
        self.disembarkationTime = disembarkationTime

    def run(self):
        while True:

            if(self.id in queue):
                self.sleep()
            else:
                queue.append(self)

    def toBoard(self, wagon):
        print("Passenger {} embarcando...".format(self.id))
        # verifica se tem lugar disponivel
        time.sleep(self.boardingTime)
        print("Passenger {} embarcou".format(self.id))


def main():
    thread1 = wagon(15, 3)
    thread2 = passenger(1, 4, 4)
    thread3 = passenger(2, 4, 4)
    thread4 = passenger(3, 4, 4)
    thread5 = passenger(4, 4, 4)

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()

    print("Exiting Main Thread")


if __name__ == '__main__':
    main()
