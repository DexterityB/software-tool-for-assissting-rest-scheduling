# when they wake
# what they do at what time
# sleep time
# activity strenuousness


# each person gets a .lsg file

# lsg format
# header:
# -days_saved:u8
# -current_day_start:u16
#
# day_table:
# -date:date
# -activities:u8
# -activity_table
# --strenuousness:i8
# --mental strain:i8
# --start:time
# --end:time
# 
#
# date:
# -d:u8
# -m:u8
# -y:u16
#
# time:
# -h:u8
# -m:u8

import os


# error codes
# 0: It worked
# 1: File already exists
# 2: File does not exist
# 3: Non-File input invalid


def init(name):
    '''
    Input name of file without .lsg
    returns error code 
    '''
    if os.path.isfile(name+".lsg"):
        return 1
    with open(name+".lsg", "wb") as f:
        f.write((0).to_bytes(1,byteorder='little',signed=False))
        f.write((3).to_bytes(2,byteorder='little',signed=False))
    return(0)

def add_day(name,date):
    '''
    Input file name without .lsg, and the date in [day_u8, month_u8, year_u16]
    returns error code
    '''
    if not os.path.isfile(name+".lsg"):
        return 2
    try:
        date[0] += 0
        date[1] += 0
        date[2] += 0
    except:
        return 3 
    with open(name+".lsg","r+b") as f:
        days_saved = int.from_bytes(f.read(1),byteorder='little',signed=False)
        days_saved += 1
        f.seek(0,0)
        f.write((days_saved).to_bytes(1,byteorder='little',signed=False))
        f.write((os.path.getsize(name+".lsg")+1).to_bytes(1,byteorder='little'))
        f.seek(0,2)
        f.write((date[0]).to_bytes(1,byteorder='little'))
        f.write((date[1]).to_bytes(1,byteorder='little'))
        f.write((date[2]).to_bytes(2,byteorder='little'))
        f.write((0).to_bytes(1,byteorder='little'))
    return 0

def add_activity(name,stren,mental,start,end):
    '''
    Input file name without .lsg,
        the strenuouse score of the activity i8,
        the mental strain of the activity i8,
        the start time [hours_u8, minutes_u8],  
        the end time [hours_u8, minutes_u8],
    Returns error code 
    '''
    if not os.path.isfile(name+".lsg"):
        return 2

    if type(stren) is not int:
        return 3

    if type(mental) is not int:
        return 3
    
    try:
        start[0] += 0
        start[1] += 0
        end[0] += 0
        end[1] += 0
    except:
        return 3
    
    with open(name+".lsg","r+b") as f:
        f.seek(1,0)
        current_day_start = int.from_bytes(f.read(2),byteorder='little')
        print(current_day_start)
        f.seek(current_day_start,0)
        f.seek(3,1)
        act_rec = int.from_bytes(f.read(1),byteorder='little')
        print(act_rec)
        act_rec += 1
        f.seek(-1,1)
        f.write((act_rec).to_bytes(1,byteorder='little'))
        f.seek(0,2)
        f.write(((stren).to_bytes(1,byteorder='little',signed=True)))
        f.write(((mental).to_bytes(1,byteorder='little',signed=True)))
        f.write(((start[0]).to_bytes(1,byteorder='little')))
        f.write(((start[1]).to_bytes(1,byteorder='little')))
        f.write(((end[0]).to_bytes(1,byteorder='little')))
        f.write(((end[1]).to_bytes(1,byteorder='little')))
    return 0


def read_lsg(name):
    '''
    Input file name without .lsg
    Returns all the file data or error:
        [
            days_saved,
            [
                [
                    [
                        d,
                        m,
                        y
                    ],
                    activites_count,
                    [
                        [
                            stren,
                            mental,
                            start_h,
                            start_m,
                            end_h,
                            end_m
                        ]
                        ...
                    ]
                ]
            ]
            ...
        ]
    '''
    
    if not os.path.isfile(name+".lsg"):
        return 2
    
    with open(name+".lsg","rb") as f:
        days_saved = int.from_bytes(f.read(1),byteorder='little')
        f.seek(2,1)
        days = []
        for d in range(0,days_saved):
            print("day")
            day = int.from_bytes(f.read(1),byteorder='little')
            month = int.from_bytes(f.read(1),byteorder='little')
            year = int.from_bytes(f.read(2),byteorder='little')

            activities = int.from_bytes(f.read(1),byteorder='little')

            acts = []
            
            for a in range(0,activities):
                stren = int.from_bytes(f.read(1),byteorder='little',signed=True)
                mental = int.from_bytes(f.read(1),byteorder='little',signed=True)

                start_h = int.from_bytes(f.read(1),byteorder='little')
                start_m = int.from_bytes(f.read(1),byteorder='little')
        
                end_h = int.from_bytes(f.read(1),byteorder='little')
                end_m = int.from_bytes(f.read(1),byteorder='little')

                acts.append([stren,mental,[start_h,start_m],[end_h,end_m]])
            days.append([[day,month,year],activities,acts])
        return [days_saved,days]



