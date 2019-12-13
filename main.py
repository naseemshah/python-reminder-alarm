import datetime
import winsound

def alarm(h,m):
    i=1
    while(i):
        dt = datetime.datetime.now()     
        if ((dt.minute==int(m)) & (dt.hour==int(h))):
            print("Its time Bitch!")
            winsound.Beep(440,500)
            i=0




print("Time to stop(HH/MM):")
h=input()
m=input()
alarm(h,m)

