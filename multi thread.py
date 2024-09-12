from threading import *
import threading
# def m1():
#     for i in range(3):
#         print("good morning...")
#
# def m2():
#     for i in range(3):
#         print("good evening...")
# def m3():
#     for i in range(3):
#         print("good night...")
# print("-----------------------------------------------------------")
# print("\tMultithreading")
# print("-----------------------------------------------------------")
# #creating objects for multiple threads
# t1=Thread(target=m1,name="morning")
# t2=Thread(target=m2,name="evening")
# t3=Thread(target=m3,name="night")
# #start the threads by calling start method
# t1.start()
# t2.start()
# t3.start()


#=====================================================================================================================


# def m1():
#     for i in range(3):
#         print("good morning...")
#
# def m2():
#     for i in range(3):
#         print("good evening...")
# def m3():
#     for i in range(3):
#         print("good night...")
# print("-----------------------------------------------------------")
# print("\tMultithreading")
# print("-----------------------------------------------------------")
# #creating objects for multiple threads
# t1=Thread(target=m1,name="morning")
# t2=Thread(target=m2,name="evening")
# t3=Thread(target=m3,name="night")
#
# #start thread 1
# t1.start()
# #wait until thread 1 is finished(main and sub threads t2,t3 should wait)
# t1.join()
# #start thread 2 after thread 1
# t2.start()
# #wait until thread 2 is finished (main and sub threads t1,t3 should wait)
# t2.join()
# #start thread 3 after thread 2
# t3.start()
# #wait until thread 3 is finished (main and sub threads t1,t2 should wait)
# t3.join()
# #end of the main thread
# print("End of the main thread...")

# import threading
# #user defined function 3
# def m1():
#     tname=threading.current_thread().getName()
#     print("Current Thread\t: ",tname)
#     print("Good Morning..")
#
# def m2():
#     tname=threading.current_thread().getName()
#     print("Current Thread\t: ",tname)
#     print("Good Evening..")
# def m3():
#     tname=threading.current_thread().getName()
#     print("Current Thread\t: ",tname)
#     print("Good Night..")
# #main thread
# print("____________________________________________________")
# print("\tFinding Current Thread - Multithreading")
# print("___________________________________________________________________________")
# #creating objects for multiple threads
# t1=Thread(target=m1,name="Morning")
# t2=Thread(target=m2,name="Evening")
# t3=Thread(target=m3,name="Night")
# #start threads
# t1.start()
# t2.start()
# t3.start()
import time
# def cal_sqre(num):
#     print("Calculate the square root of the given number")
#     for n in num:
#         time.sleep(0.3)#at each iteration it waits for 0.3 time
#         print('Square is :',n*n)
#
# def cal_cube(num):
#     print("Calculate the cube  of the given number")
#     for n in  num:
#         time.sleep(0.3)#at each iteration it waits for 0.3 time
#         print("cube is : ",n*n*n)
#
# arg=[4,5,6,7,2]
# t=time.time()#get total to exectue the function
# cal_cube(arg)
# cal_sqre(arg)
# th1=threading.Thread(target=cal_sqre,args=(arg, ))
# th2=threading.Thread(target=cal_cube,args=(arg, ))
# th1.start()
# th2.start()
# th1.join()
# th2.join()
# print("Total time taking by threads is:",time.time() -t)#print the total time
# print("Again executing the main thread")
# print("Thread 1 and Thread 2 have finished their execution")
#
# print("_______________________________________________________________________________________")
#
import _thread
import time

# def my_thread(thrd_mssg,delay):
#     count=0
#     while count<3:
#         time.sleep(delay)
#         count+=1
#         #print--will dsplay which thread ia executed and time taken
#         print(thrd_mssg,"-----------------------",time.time())
#
# #now the thread fun need to be exected
# try:
#     _thread.start_new_thread(my_thread,("thread 1",1))
#     _thread.start_new_thread(my_thread,("thread 2",2))
#
# except:
#     print("some error occured")
#
# while 1:
#     pass
import time

def calc_square(numbers,delay):
    for n in numbers:
        print(f'\n{n} ^ 2 = {n*n}')
        time.sleep(delay)

def calc_cube(numbers,delay):
    for n in numbers:
        print(f'\n{n} ^ 3 = {n*n*n}')
        time.sleep(delay)

numbers=[2,3,4,5,8]

square_thread = threading.Thread(target=calc_square,args=(numbers,1))
cube_thread = threading.Thread(target=calc_cube,args=(numbers,2))

square_thread.start()

cube_thread.start()

square_thread.join()
cube_thread.join()
print("Thread Execution Done")


