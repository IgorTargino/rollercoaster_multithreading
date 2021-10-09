import threading
import time

exitFlag = False


class wagon (threading.Thread):
    def __init__(self, travelTime, maxCapacity):
        threading.Thread.__init__(self)
        self.travelTime = travelTime
        self.maxCapacity = maxCapacity

    def run(self):
        while True:
            print("Starting rollercoaster")
            time.sleep(2)
            print("Exiting rollercoaster")


class passenger (threading.Thread):
    def __init__(self, id, boardingTime, disembarkationTime):
        threading.Thread.__init__(self)
        self.id = id
        self.boardingTime = boardingTime
        self.disembarkationTime = disembarkationTime

    def run(self):
        while True:
            print("Starting passenger")
            time.sleep(2)
            print("Exiting passenger")


def main():
    thread1 = wagon(15, 5)
    thread2 = passenger(1, 4, 4)

    thread1.start()
    thread2.start()

    print("Exiting Main Thread")


if __name__ == '__main__':
    main()
