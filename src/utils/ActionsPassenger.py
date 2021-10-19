from threads.Passenger import Passenger


def actionQueue(method, queue):
    if(method == "sleep"):
        for passenger in queue:
            passenger.sleep()
    elif(method == "wakeUp"):
        for passenger in queue:
            passenger.wakeUp()


def actionCurrentPassenger(method, currentPassengers):
    if(method == "sleep"):
        for passenger in currentPassengers:
            passenger.sleep()
    elif(method == "wakeUp"):
        for passenger in currentPassengers:
            passenger.wakeUp()


def newPassenger(boardingTime, disembarkationTime, queue):
    print("Inserindo novo passageiro")
    currentPassenger = Passenger(boardingTime, disembarkationTime)
    queue.append(currentPassenger)
    currentPassenger.start()
    currentPassenger.join()
