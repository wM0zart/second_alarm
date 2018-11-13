
import time
from tkinter import *
from tkinter import messagebox
from datetime import datetime

def timer1(s):
    time.sleep(s)

def wainting(count_time, type_time):
    start_time = datetime.now()
    print("Start executing...: " + str(start_time))
    if type_time == 'min':
        timer1(60*count_time)
    elif type_time == 'sec':
        timer1(count_time)
    elif type_time == 'hour':
        timer1(60*60*count_time)
    messagebox.showinfo("warning!!" , "You need!!")
    print("End  executing...: " + str(datetime.now()))


if __name__ == '__main__':
    lenline = len(sys.argv)
    if lenline<=2:
        wainting(60, 'sec')
    elif lenline >= 2:
        if sys.argv[2] in ('min', 'sec', 'hour'):
            wainting(int(sys.argv[1]), sys.argv[2])
    else:
        print("Mistake parameter")
