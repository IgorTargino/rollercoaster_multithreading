from threads.Passenger import Passenger


class ActionsPassenger():
    def __init__(self):
        super().__init__()

    def action_queue(self, method, queue):
        if(method == "sleep"):
            for passenger in queue:
                passenger.sleep()
        elif(method == "wakeUp"):
            for passenger in queue:
                passenger.wakeUp()

    def action_current_passenger(self, method, current_passengers):
        if(method == "sleep"):
            for passenger in current_passengers:
                passenger.sleep()
        elif(method == "wakeUp"):
            for passenger in current_passengers:
                passenger.wakeUp()

    def new_passenger(self, queue, current_id, boarding_time, disembarkation_time, mutex, wagon):
        print("Inserindo novo passageiro")
        current_passenger = Passenger(
            queue, current_id, boarding_time, disembarkation_time, mutex, wagon)
        queue.append(current_passenger)
        current_id += 1
        current_passenger.start()
        current_passenger.join()
