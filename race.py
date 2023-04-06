# Threads with a race condition!!
import threading
import time

print('Start of program.')
myList = []


def raceFunc(i, myList):
    myList.append(i)
    # print('    Start doing something in thread {} with list {} '.format(i, myList))
    # address of list: hex(id(myList)) - try to print it!
    print('    Start doing something in thread {} (i at {}), '
          'with list {} at {}'.format(i, hex(id(i)), myList, hex(id(myList))))
    time.sleep(3)
    print('    Thread {} finished with list {}'.format(i, myList))
    # Is Python call by reference or call by value?
    # https://www.geeksforgeeks.org/is-python-call-by-reference-or-call-by-value/


threads = [None] * 5
for i in range(len(threads)):
    #myList.append(i)
    threads[i] = threading.Thread(target=raceFunc, args=(i,myList))
    threads[i].start()

# do some other stuff
print('*' * 50)

[thread.join() for thread in threads]
print('End of program.')
