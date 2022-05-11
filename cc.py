#coding:utf-8

import random
import autopy
import keyboard
import _thread
from time import sleep

global jack
jack=0

def doo(dd,ww):
    global jack
    if jack==1:
        jack=0
    else:
        jack=1
    print("whoami")
def mainloop(df,ef):
    global jack
    while(1):
        while(jack==1):
            c=random.randint(1,10)
            if c<=5:
                y=random.randint(0,899)
                x=random.randint(0,1400)
                autopy.mouse.smooth_move(x,y)
                sleep(3)
            elif c<=7:
                autopy.mouse.click()
                sleep(3)
            else:
                key=random.choice('wasd')
                keyboard.press_and_release(key)
                sleep(3)
try:
   _thread.start_new_thread( mainloop, ("Thread-1", 2, ) )
except:
   print ("Error: 无法启动线程")
   
print("running waiting hotkey ctrl+f10,+f3 to exit.")
c=keyboard.add_hotkey('ctrl+f10', doo, args=('triggered', 'hotkey'))

keyboard.wait("ctrl+f3")



# #!/usr/bin/python3

# import _thread
# import time

# # 为线程定义一个函数
# def print_time( threadName, delay):
   # count = 0
   # while count < 5:
      # time.sleep(delay)
      # count += 1
      # print ("%s: %s" % ( threadName, time.ctime(time.time()) ))

# # 创建两个线程
# try:
   # _thread.start_new_thread( print_time, ("Thread-1", 2, ) )
   # _thread.start_new_thread( print_time, ("Thread-2", 4, ) )
# except:
   # print ("Error: 无法启动线程")

# while 1:
   # pass