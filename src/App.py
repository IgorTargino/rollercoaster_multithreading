import time
from threading import Lock, Semaphore
from threads.Wagon import Wagon
from utils.ActionsPassenger import ActionsPassenger


queue = []
mutex = Lock()

semaphore_wagon = Semaphore(1)


class App():

    def __init__(self):
        print("Iniciando aplicação!!")

        wagon = Wagon(10, 3, mutex, semaphore_wagon, queue)

        ActionsPassenger.new_passenger(queue, 5, 5, mutex, wagon)
        ActionsPassenger.new_passenger(queue, 5, 5, mutex, wagon)
        ActionsPassenger.new_passenger(queue, 5, 5, mutex, wagon)


App()
