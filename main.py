#!/usr/bin/env python3


#DB
import pymongo
dbclient = pymongo.MongoClient("mongodb://localhost:27017/")
db = dbclient["reminderdbxx"]
col = db["remindersxx"]
col.insert_one({"reminder": "Dummy Reminder", "time": "2454" })
col.delete_many({"reminder": "Dummy Reminder"})

def insert():
        rem=input("Enter the reminder:\n")
        print("When time do you to be reminded [24 hours]?:")


        th=input("\thh:")
        while((len(str(th))!=2) | (int(th)<0) | (int(th)>60)):
                if (len(str(th))!=2):
                        print("\tPlease enter only two digits (hh).\n")
                        th=input("\thh:")
                elif ((int(th)<0) | (int(th)>60)):
                        print("\tInvalid input\n")
                        th=input("\thh:")


        tm=input("\tmm:")
        while((len(str(tm))!=2) | (int(tm)<0) | (int(tm)>60)):
                              if (len(str(th))!=2):
                                      print("\tPlease enter only two digits (mm).\n")
                                      tm=input("\tmm:")
                              elif (int(tm)<0) | (int(tm)>60) :
                                      print("\tInvalid input. (mm)\n")
                                      tm=input("\tmm:")
        col.insert_one({ "id": col.find().count()+1 , "reminder": rem, "timeh" : th ,"timem" : tm })

def chkdb():
        dblist = dbclient.list_database_names()
        if "reminderdb" in dblist:
                print("The database Connected!")

        else:
                print("Conncetion to Database Failed :(")
def list():
        reminders=col.find()
        if col.find().count()==0:
                print("No Reminder has been added")
        else:
                print("\nActive Reminders:\n----------\n")
                for i in reminders:
                        print("("+str(i['id'])+")----------------\n\n",i['reminder'],"\n\n Time:",str(i['timeh'])+":"+str(i['timem']),"\n------------------\n")

def updateR(ind,newrem):
        col.update_one({'id' : int(ind)}, { "$set": {"reminder": str(newrem)} })

def updateT(ind,newh,newm):
        col.update_one({'id' : int(ind)}, { "$set": {"timeh" : str(newth) ,"timem" : str(newtm) } })

def updateRT(ind,newrem,newh,newm):
        col.update_one({'id' : int(ind)}, { "$set": {"reminder": str(newrem), "timeh" : str(newth) ,"timem" : str(newtm) } })

        
        

def alarm(h,m):
    i=1
    while(i):
        dt = datetime.datetime.now()
        if ((dt.minute==int(m)) & (dt.hour==int(h))):
            print("Its time Bitch!")
            playsound('audio.mp3')
            i=0
chkdb()
print("\nWelcome to Reminders CLI APP\n")
loop=1
while(loop):
        print("\nPlease Choose\n\t1)Retrieve Reminders \n\t2)Update Reminders\n\t3)Add Reminders\n\t4)Exit")
        ch=input("\t")
        while((int(ch)<1) | (int(ch)>4)):
                print("\n\tInvalid Choice\n\tPlease Choose(1/2/3)")
                ch=input("\n\t")
        if(int(ch)==1):
                list()
        elif(int(ch)==2):
                index=input("\n\tEnter the Index of the Reminder to Change:")
                while((int(col.find().count()) < int(index))|(int(index)<1)):
                        print("\n\t Invalid Index.")
                        index=input("\n\tEnter Index:")
                
                print("\n\tWhat dow you want to change?\n\t\t1)Reminder Content\n\t\t2)Time\n\t\t3)Both")
                ch2 = input("\n\t\t")
                while(((int(ch2)<1) | (int(ch2)>3))):
                        print("\n\tInvalid Choice\n\tPlease Choose(1/2/3)")
                        ch2=input("\n\t\t")
                if int(ch2)==1:
                        newreminder=input("\n\t\tEnter new reminder:\n\t\t")
                        updateR(index,newreminder)
                elif int(ch2)==2:
                        print("What is the new time [24 hours]?:")
                        newth=input("\thh:")
                        while((len(str(newth))!=2) | (int(newth)<0) | (int(newth)>60)):
                                if (len(str(newth))!=2):
                                        print("\tPlease enter only two digits (hh).\n")
                                        newth=input("\thh:")
                                elif ((int(newth)<0) | (int(newth)>60)):
                                        print("\tInvalid input\n")
                                        newth=input("\thh:")


                        newtm=input("\tmm:")
                        while((len(str(newtm))!=2) | (int(newtm)<0) | (int(newtm)>60)):
                                              if (len(str(newth))!=2):
                                                      print("\tPlease enter only two digits (mm).\n")
                                                      newtm=input("\tmm:")
                                              elif (int(newtm)<0) | (int(newtm)>60) :
                                                      print("\tInvalid input. (mm)\n")
                                                      newtm=input("\tmm:")
                        updateT(index,newth,newtm)
                else:
                        newreminder=input("\n\t\tEnter new reminder:\n\t\t")
                        print("What is the new time [24 hours]?:")
                        newth=input("\thh:")
                        while((len(str(newth))!=2) | (int(newth)<0) | (int(newth)>60)):
                                if (len(str(newth))!=2):
                                        print("\tPlease enter only two digits (hh).\n")
                                        newth=input("\thh:")
                                elif ((int(newth)<0) | (int(newth)>60)):
                                        print("\tInvalid input\n")
                                        newth=input("\thh:")


                        newtm=input("\tmm:")
                        while((len(str(newtm))!=2) | (int(newtm)<0) | (int(newtm)>60)):
                                              if (len(str(newth))!=2):
                                                      print("\tPlease enter only two digits (mm).\n")
                                                      newtm=input("\tmm:")
                                              elif (int(newtm)<0) | (int(newtm)>60) :
                                                      print("\tInvalid input. (mm)\n")
                                                      newtm=input("\tmm:")
                        updateRT(index,newreminder,newth,newtm)
        elif(int(ch)==3):
                insert()
        elif(int(ch)==4):
                print("\nExiting.....\nGood Bye!")
                loop=0
                        
                
                        
        
        

#print("Time to stop(HH/MM):")
#h=input()
#m=input()
#alarm(h,m)

