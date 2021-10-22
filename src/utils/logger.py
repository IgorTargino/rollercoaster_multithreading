import datetime


def logger_passenger(thread, msg):
    current_date = datetime.datetime.now().strftime('%Y-%m-%d-%H%M')
    file = open("./src/logs/passenger-{}.txt".format(current_date), 'a')

    thread_str = str(thread)

    print("\n" + thread_str+msg + "\n")
    file.write("\n" + thread_str+msg + "\n")
    file.close()


def logger_wagon(thread, msg):
    current_date = datetime.datetime.now().strftime('%Y-%m-%d-%H%M')
    file = open("./src/logs/wagon-{}.txt".format(current_date), 'a')

    thread_str = str(thread)

    print("\n" + thread_str+msg + "\n")
    file.write("\n" + thread_str+msg + "\n")
    file.close()
