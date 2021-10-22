from threading import Semaphore, Thread, Lock, Event, active_count, current_thread
import threading
import time
import random
from utils.logger import logger_passenger


class Passenger(Thread):

    def __init__(self, queue, id, boarding_time, disembarkation_time, mutex, wagon):

        Thread.__init__(self)

        self.id: int = id
        self.boarding_time: int = boarding_time
        self.disembarkation_time: int = disembarkation_time

        self.mutex: Lock = mutex
        self.wagon = wagon

        self.queue: list = queue

        self.acontecimentos: dict = {1: "derrubou o telefone", 2: "vomitou",
                                     3: "gritou", 4: "desmaiou", 5: "chingou todo mundo"}

        self.start()

    def run(self):

        while True:

            self.mutex.acquire()
            logger_passenger(self, "Thread passageiro {}".format(self.id))
            logger_passenger(
                self, "Fila de embarque: {}".format(self.queue))
            logger_passenger(self, "Passageiros no vagão: {}".format(
                self.wagon.current_passengers))
            logger_passenger(self,
                             "Estado do vagão: {}".format(self.wagon.state))
            logger_passenger(self,
                             "Numero de acentos no vagão: {}".format(self.wagon.seats))
            self.mutex.release()

            if(self.wagon.state == "BOARDING"):
                if(self.queue[0] == self and self.wagon.seats > 0):
                    self.to_board()

                    if(self.wagon.seats == 0):
                        self.wagon.state = "WALKING"
                        self.wagon.semaphore_wagon.release()

            if(self.wagon.state == "WALKING"):
                if(self in self.wagon.current_passengers):
                    self.enjoy_the_landscape()

            if(self.wagon.state == "LANDING"):
                if(self.wagon.current_passengers[-1] == self):
                    self.land()

                if(self.wagon.seats == self.wagon.max_capacity):
                    self.wagon.state = "BOARDING"

    def to_board(self):

        self.mutex.acquire()
        logger_passenger(self, "Passageiro {} embarcando".format(self.id))
        self.queue.remove(self)
        self.mutex.release()

        self.wagon.current_passengers.append(self)
        self.wagon.seats -= 1

        initial_time = time.time()

        self.mutex.acquire()
        while(time.time() - initial_time < self.boarding_time):
            time.sleep(1)
        logger_passenger(self, "Passageiro {} embarcou".format(self.id))
        self.mutex.release()

    def land(self):

        self.mutex.acquire()
        logger_passenger(self, "Passageiro {} desembarcando".format(self.id))
        self.mutex.release()

        initial_time = time.time()

        self.mutex.acquire()
        while(time.time() - initial_time < self.disembarkation_time):
            time.sleep(1)
        logger_passenger(self, "Passageiro {} desembarcou".format(self.id))
        self.mutex.release()

        self.wagon.current_passengers.remove(self)
        self.wagon.seats += 1

        self.mutex.acquire()
        self.queue.append(self)
        self.mutex.release()

    def enjoy_the_landscape(self):
        aux = random.randint(0, 5)

        self.mutex.acquire()
        logger_passenger(
            self, "Thread passageiro {} entrou no landscape e o aux é: {}!".format(self.id, aux))
        self.mutex.release()

        if(aux in self.acontecimentos):

            self.mutex.acquire()
            logger_passenger(self, "passageiro {} {}".format(
                self.id, self.acontecimentos[aux]))
            self.mutex.release()
