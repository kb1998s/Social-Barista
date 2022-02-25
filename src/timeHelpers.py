from datetime import date
from datetime import datetime as dt
import datetime 



def categorizeDay(curr):
    res = ''
    if curr.weekday() > 4:
        res = "WEEKEND"
    else:
        res = "WEEKDAY"
    return res

time = dt.now()

def CategorizeTime(current):
    res = ''
    morningStart = datetime.time(4, 0 ,0)
    morningEnd = datetime.time(11,0,0)
    if morningStart <= current <= morningEnd:
        res = "MORNING"
    
    noonStart = datetime.time(11, 0 ,0)
    noonEnd = datetime.time(16,0,0)
    if noonStart <= current <= noonEnd:
        res = "NOON"
        
    nightStart = datetime.time(16, 0 ,0)
    nightEnd = datetime.time(23,0,0)
    if nightStart <= current <= nightEnd:
        res = "NIGHT"
        
    lateStart = datetime.time(23, 0 ,0)
    lateEnd = datetime.time(4,0,0)
    if lateStart <= current <= lateEnd:
        res = "LATENIGHT"
    
    return res

def getTimeCategory():
    day = date.today()
    time = dt.now().time()
    day = categorizeDay(day)
    time = CategorizeTime(time)
    return day + "_" + time

print(getTimeCategory())