#
# Title:room_schedule.py
# Description: conference room scheduler
#

MAX_SLOTS = 8
schedule = []

def setup_schedule():
    for ndx in range(MAX_SLOTS):
        schedule.append(False)

def matcher(start, duration: int) -> bool:
    if start + duration >= MAX_SLOTS:
        return False
    
    for ndx in range(start, start + duration):
        if schedule[ndx] == True:
            return False
        
    for ndx in range(start, start + duration):
        schedule[ndx] = True

    return True

def schedule_room(duration:int) -> bool:
    for ndx1 in range(len(schedule)):
        if schedule[ndx1] == False:
            if matcher(ndx1, duration):
                return True

    print("schedule_room")
    return False

if __name__ == '__main__':
    print("main")

    setup_schedule()

    print(schedule)
    print(schedule_room(1))
    print(schedule)

    print(schedule_room(2))
    print(schedule)

    schedule[1] = False
    print(schedule_room(2))
    print(schedule)

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
