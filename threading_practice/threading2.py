import time
import threading


# want to do 2 different jobs. I want to calculate the squares of these numbers and the cubes of the numbers at the same time.

def calc_square(nums):
    print("Calculate square numbers")
    for n in nums:
        time.sleep(0.2)
        print('Square: ' + str(n**2) + "\n", end="")

def calc_cube(nums):
    print("Calculate cube of numbers")
    for n in nums:
        time.sleep(0.2)
        print("Cube: " + str(n**3) + "\n", end="")
        
numList = [2,3,8,9]

t = time.time()
t1 = threading.Thread(target=calc_square, args=(numList,)) #This is sort of like assigning the first task to the busy mom. You have to provide the arguments as a tuple unfortunately, it's just a thing.
t2 = threading.Thread(target=calc_cube, args=(numList,)) #This is sort of like assigning the second task to the busy mom. args are in a tuple again.

t1.start() # this tells your thread to kick off and get to work
t2.start()

t1.join() # this says "wait until you're both finished and then give your results at the same time.
t2.join()

#calc_square(numList)
#calc_cube(numList)
print("Done in: " + str(time.time() - t))
print("Hah... I am done with all my work now!")

#taking 1.6 seconds to execute. Now I want to use multithreading.
# now that it's threaded, you have the program using the idle time that one is using, the sleep part, to print in the other funtion, so they now altenate when printing.
# python multithreading is gonna have issue, need to look into processing library, not threading, because python really only runs one thread
