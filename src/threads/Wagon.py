from threading import Event, Semaphore, Thread, Lock
from utils.logger import logger_wagon
import time


class Wagon(Thread):

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
                self.mutex.acquire()
                logger_wagon(self, "Fila de embarque: {}".format(self.queue))
                logger_wagon(self, "Passageiros no vagão: {}".format(
                    self.current_passengers))
                logger_wagon(self, "Estado do vagão: {}".format(self.state))
                logger_wagon(self,
                             "Numero de acentos no vagão: {}".format(self.seats))
                self.mutex.release()

                self.start_roller_coaster()
                self.stop_roller_coaster()

    def start_roller_coaster(self):

        self.mutex.acquire()
        logger_wagon(self, "Iniciando montanha russa")

        logger_wagon(self, "Fila de embarque: {}".format(self.queue))
        logger_wagon(self, "Passageiros no vagão: {}".format(
            self.current_passengers))
        logger_wagon(self, "Percorrendo montanha...")
        self.mutex.release()

        # time.sleep(self.travel_time)
        initial_time = time.time()

        self.mutex.acquire()
        while(time.time() - initial_time < self.travel_time):
            time.sleep(1)
        self.mutex.release()

    def stop_roller_coaster(self):
        self.mutex.acquire()

        logger_wagon(self, "Fila de embarque: {}".format(self.queue))
        logger_wagon(self, "Passageiros no vagão: {}".format(
            self.current_passengers))
        logger_wagon(self, "Montanha russa finalizada")

        self.mutex.release()

        self.state = "LANDING"
