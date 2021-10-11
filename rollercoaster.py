import threading
import time

currentId = 0
#queue = []

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

#INCIO DO VAGAO PARA EMBARCAR OS PASSAGEIROS
    def wagonStart(self, wagon):
        #print("Vagão está aberto!")
        passengerThreads = []  
        for passenger in wagon.maxCapacity:
            passengerthread = threading.Thread(target=self.toBoard(wagon), args=(wagon,))
            passengerthread.start()
        for passT in passengerThreads:   # joining threads
            passT.join()
    
#EMBARCAR O PASSAGEIRO
    
    def toBoard(self, wagon):

        mutex.acquire()
        
        print("Passenger {} está procurando um assento...".format(self.id))
        #CHECAGEM DE ASSENTO
        if len(wagon.capacityList) == wagon.maxCapacity:
            self.sleep()
            print("Assento cheio, Passenger {} esperando".format(self.id))
        else:
            print("Passenger {} embarcando...".format(self.id))
            time.sleep(self.boardingTime)
            wagon.capacityList.append(self)
            print("Passenger {} embarcou".format(self.id))
            mutex.release()
        
            
    def available(self):
        
        return self.passengerWorkingEvent.isSet()

    
    def sleep(self):
        
        self.passengerWorkingEvent.wait()

    
    def wakeUp(self):
        self.passengerWorkingEvent.set()
    


def main():
    #CRIANDO UMA LISTA PARA OS ASSENTOS
    capacityList = []
    n_seats = input("Quantos assentos você quer no vagão?\n")
    wag = wagon(10, n_seats)

    
    
    #thread2 = passenger0(1, 4, 4)
    #thread3 = passenger1(2, 4, 4)
    #thread4 = passenger(3, 4, 4)
    #thread5 = passenger(4, 4, 4)

    #CRIANDO A FILA DE ESPERA NO MAIN E ADICIONANDO DOIS PASSAGEIROS
    queue = []
    passageiro1 = passenger(1, 4, 4)
    passageiro2 = passenger(2, 4, 12)
    queue.append(passageiro1)
    queue.append(passageiro2)
    #thread1.start()
    #thread2.start()
    #thread3.start()
    #thread4.start()
    #thread5.start()
    while len(queue) > 0:
        nextPassenger = queue.pop()
        nextPassenger.wagonStart(wag)
        #nextPassenger.toBoard(wag)
        
        
    

    #print("Exiting Main Thread")


if __name__ == '__main__':
    main()
