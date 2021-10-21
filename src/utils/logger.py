import datetime


def logger(id: int, queue: list, state: str, seats: int):
    current_date = datetime.datetime.now().strftime('%Y-%m-%d-%H%M')
    file = open("{}.txt".format(current_date), 'a')

    print("==============================================")
    print("Thread passageiro {}".format(id))
    print("Fila de passageiros: {}".format(queue))
    print("Estado do vagão: {}".format(state))
    print("Numero de acentos no vagão: {}".format(seats))
    print("==============================================")

    file.write("============================================== \n")
    file.write("Thread passageiro {} \n".format(id))
    file.write("Fila de passageiros: {} \n".format(queue))
    file.write("Estado do vagão: {} \n".format(state))
    file.write("Numero de acentos no vagão: {} \n".format(seats))
    file.write("============================================== \n")

    file.close()
