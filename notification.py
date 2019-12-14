#date time
import datetime

#play sound
from playsound import playsound
#notifications
import notify2
notify2.init('Reminders CLI')
import pymongo
dbclient = pymongo.MongoClient("mongodb://localhost:27017/")
db = dbclient["reminderdbxx"]
col = db["remindersxx"]
col.insert_one({"reminder": "Dummy Reminder", "time": "2454" })
col.delete_many({"reminder": "Dummy Reminder"})

def find(h,m):
    data=col.find({'timeh': str(h) , 'timem': str(m)})
    count=data.count()
    if(data):       
        title = "You have " + str(count) + " Reminders\n"
        message = ''
        for x in range(0,data.count()):
            message+="\n \u2022 "+data[x]['reminder']
        n = notify2.Notification(title, message)
        n.show()       
        alarm()


def alarm():
    playsound('audio.mp3')

while(loop)
