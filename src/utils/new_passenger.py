from threading import current_thread
from threads.Passenger import Passenger
current_id = 0


def new_passenger(queue,  boarding_time, disembarkation_time, mutex, wagon):
    global current_id

    print("Inserindo novo passageiro")
    current_passenger = Passenger(
        queue, current_id, boarding_time, disembarkation_time, mutex, wagon)
    queue.append(current_passenger)
    current_id += 1
