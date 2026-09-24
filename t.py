import lsg

name = input("Input name: ").strip()

i = lsg.init(name)

if i == "yay":
    print("lsg file not found creating one.")

i = input("new day?\n")
if i[0].lower() == "y":
    date = input("what is the date (dd/mm/yy): ").strip().split('/')
    
    lsg.add_day(name, [int(date[0]),int(date[1]),int(date[2])])

i = input("add activity?\n")
if i[0].lower() == "y":
    s = int(input("stren: "))
    m = int(input("mental: "))
    start = input("start time (hh/mm)").strip().split('/')
    end = input("end time (hh/mm)").strip().split('/')

    lsg.add_activity(name, s, m, [int(start[0]),int(start[1])], [int(end[0]), int(end[1])])

print(lsg.read_lsg(name))
