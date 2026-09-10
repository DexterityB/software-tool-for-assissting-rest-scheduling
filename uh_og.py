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

name = "hello"

def init(name):
    if os.path.isfile(name+".lsg"):
        return "already exists"
    with open(name+".lsg", "wb") as f:
        f.write((0).to_bytes(1,byteorder='little',signed=False))
        f.write((3).to_bytes(2,byteorder='little',signed=False))
    return("yay")

def add_day(name,date):
    if not os.path.isfile(name+".lsg"):
        return "no file"
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

def add_activity(name,stren,start,end):
    with open(name+".lsg","r+b") as f:
        f.seek(1,0)
        current_day_start = int.from_bytes(f.read(2),byteorder='little')
        f.seek(current_day_start,0)
        
        

print(init(name))
print(add_day(name, [1,2,3]))



