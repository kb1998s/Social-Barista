from datetime import date
from datetime import datetime as dt
import datetime 


# get day type category:
def categorizeDay(cur):
    res = ''
    if cur.weekday() > 4:
        res = "WEEKEND"
    else:
        res = "WEEKDAY"
    return res

time = dt.now()

# get time-based category
def CategorizeTime(current):
    res = ''
    morningStart = datetime.time(5, 0 ,0)
    morningEnd = datetime.time(11,59,59)
    if morningStart <= current <= morningEnd:
        res = "MORNING"
    
    noonStart = datetime.time(12, 0 ,0)
    noonEnd = datetime.time(16,59,59)
    if noonStart <= current <= noonEnd:
        res = "NOON"
        
    nightStart = datetime.time(17, 0 ,0)
    nightEnd = datetime.time(23,59,59)
    if nightStart <= current <= nightEnd:
        res = "NIGHT"
        
    lateStart = datetime.time(0, 0 ,0)
    lateEnd = datetime.time(4,59,59)
    if lateStart <= current <= lateEnd:
        res = "NIGHT"
    
    return res

def getTimeCategory():
    day = date.today()
    time = dt.now().time()
    day = categorizeDay(day)
    time = CategorizeTime(time)
    return day + "_" + time

def getGreeting():
    cur = getTimeCategory()
    switcher = {
        "WEEKDAY_MORNING": "Good morning!",
        "WEEKDAY_NOON": "Good afternoon!",
        "WEEKDAY_NIGHT": "Good evening!",
        "WEEKEND_MORNING": "It's a lovely weekend morning!",
        "WEEKEND_NOON": "It's a lovely weekend afternoon!",
        "WEEKEND_NIGHT": "It's a lovely weekend evening!",
    }
    
    return switcher.get(cur, "Hi")

print(getTimeCategory())