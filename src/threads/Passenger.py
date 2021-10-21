from threading import Thread, Lock, Event
import time
import random


class Passenger(Thread):

    passengerEvent = Event()

    def __init__(self, queue, id, boarding_time, disembarkation_time, mutex, wagon):

        Thread.__init__(self)

        self.id: int = id
        self.boardingTime: int = boarding_time
        self.disembarkationTime: int = disembarkation_time

        self.mutex: Lock = mutex
        self.wagon = wagon

        self.queue: list = queue

        self.acontecimentos: dict = {20: "derrubou o telefone", 60: "vomitou",
                                     115: "gritou", 176: "desmaiou", 233: "chingou todo mundo"}

        self.start()

    def run(self):
        print("Thread passageiro {} iniciada!".format(self.id))

        while True:
            # self.mutex.acquire()

            if(self.queue[0] == self and self.wagon.state == "BOARDING" and self.wagon.seats < 0):
                self.to_board()

                if(self.wagon.seats == 0):
                    self.wagon.state = "WALKING"
                    self.wagon.semaphore_wagon.release()

                    self.enjoy_the_landscape()
                    self.land()

                if(self.wagon.seats == self.wagon.max_capacity):
                    self.wagon.state = "BOARDING"

    def to_board(self):
        print("Passageiro {} embarcando".format(self.id))

        self.mutex.acquire()
        self.queue.remove(self)
        self.mutex.release()

        self.wagon.current_passengers.append(self)
        self.wagon.seats -= 1

        time.sleep(self.boardingTime)

    def land(self):
        print("Passageiro {} desembarcando".format(self.id))

        self.wagon.current_passengers.remove(self)
        self.wagon.seats += 1

        self.mutex.acquire()
        self.queue.apeend(self)
        self.mutex.release()

        time.sleep(self.disembarkationTime)

    def enjoy_the_landscape(self):
        while(self.wagon.state == "WALKING"):
            aux = random.randint(0, 10000000)
            if(aux in self.acontecimentos):
                print("passageiro {} {}".format(
                    self.id, self.acontecimentos[aux]))

    def available(self):
        return self.passengerEvent.isSet()

    def sleep(self):
        print("Thread passageiro {} dormindo".format(self.id))
        self.passengerEvent.wait()

    def wakeUp(self):
        print("Thread passageiro {} acordada".format(self.id))
        self.passengerEvent.set()
