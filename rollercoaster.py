import threading
import time

currentId = 0


mutex = threading.Lock()


class wagon (threading.Thread):

    wagonWorkingEvent = threading.Event()
    capacityList = []

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
        return self.wagonWorkingEvent.isSet()
            
    def sleep(self):
       
        self.wagonWorkingEvent.wait()

    def wakeUp(self):
        self.wagonWorkingEvent.set()

#INCIO DO VAGAO PARA EMBARCAR OS PASSAGEIROS
    #def wagonStart(self, passenger):
        #print("Vagão está aberto!")
       # wagonThreads = []  
       # for wagon in self.maxCapacity:
       #     wagonthread = threading.Thread(target=self.toBoard, args=(passenger,))
       #     wagonthread.start()
       # for wT in wagonThreads:   # joining threads
      #      wT.join()

    

#DESEMBARCAR O PASSAGEIRO
    def toQueue(self):

        print("Fim da viagem!")
        while True:
            mutex.acquire()     

            if len(self.capacityList) > 0:
                nextCust = self.capacityList[0]
                print("Passenger {} está desembarcando...".format(nextCust.id))
                timeDesembark = nextCust.disembarkationTime
                time.sleep(timeDesembark)
                del self.capacityList[0]
                print("Passenger {} desembarcou...".format(nextCust.id))
                mutex.release()     
            else:
                mutex.release()
    
#EMBARCAR O PASSAGEIRO
    
    def toBoard(self, passenger):

        mutex.acquire()
        
        print("Passenger {} está procurando um assento...".format(passenger.id))
        #CHECAGEM DE ASSENTO
        if len(self.capacityList) == self.maxCapacity:
            print("Vagão cheio, Passenger {} esperando...".format(passenger.id))
            mutex.release()
        else:
            print("Passenger {} embarcando...".format(passenger.id))
            time.sleep(passenger.boardingTime)
            self.capacityList.append(passenger)
            mutex.release()
            print("Passenger {} embarcou...".format(passenger.id))
            
        
class passenger (threading.Thread):

    passengerWorkingEvent = threading.Event()

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
           
    def available(self):
        
        return self.passengerWorkingEvent.isSet()

    
    def sleep(self):
        
        self.passengerWorkingEvent.wait()

    
    def wakeUp(self):
        self.passengerWorkingEvent.set()
    


def main():
    #CRIANDO UMA CAPACIDADE PARA OS ASSENTOS
    n_seats = int(input("Qual é a capacidade máxima do vagão?\n"))
    wag = wagon(10, n_seats)

    
    
    #thread2 = passenger0(1, 4, 4)
    #thread3 = passenger1(2, 4, 4)
    #thread4 = passenger(3, 4, 4)
    #thread5 = passenger(4, 4, 4)

    #CRIANDO A FILA DE ESPERA NO MAIN E ADICIONANDO DOIS PASSAGEIROS
    queue = []
    passageiro1 = passenger(1, 4, 2)
    passageiro2 = passenger(2, 4, 5)
    passageiro3 = passenger(3, 4, 10)
    passageiro4 = passenger(4, 4, 15)
    passageiro5 = passenger(5, 4, 25)
    passageiro6 = passenger(6, 4, 7)
    queue.append(passageiro1)
    queue.append(passageiro2)
    queue.append(passageiro3)
    queue.append(passageiro4)
    queue.append(passageiro5)
    queue.append(passageiro6)
    #thread1.start()
    #thread2.start()
    #thread3.start()
    #thread4.start()
    #thread5.start()
    while len(queue) > 0:
        nextPassenger = queue.pop()
        wag.toBoard(nextPassenger)
    if len (queue) == 0:
        wag.toQueue()
        #nextPassenger.toBoard(wag)
        
        
    

    #print("Exiting Main Thread")


if __name__ == '__main__':
    main()
