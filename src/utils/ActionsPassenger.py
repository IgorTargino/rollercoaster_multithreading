from threading import current_thread
from threads.Passenger import Passenger
from utils.logger import logger_passenger
current_id = 0


def action_list(method, list):
    if(method == "sleep"):
        for passenger in list:
            passenger.semaphore_passenger.acquire()
    elif(method == "wakeUp"):
        for passenger in list:
            passenger.semaphore_passenger.release()


def new_passenger(queue,  boarding_time, disembarkation_time, mutex, wagon):
    global current_id

    print("Inserindo novo passageiro")
    current_passenger = Passenger(
        queue, current_id, boarding_time, disembarkation_time, mutex, wagon)
    queue.append(current_passenger)
    current_id += 1
