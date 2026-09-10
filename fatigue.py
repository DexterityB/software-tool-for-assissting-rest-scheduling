def find_total_stren(start_times, end_times, stren_per_hour):
    real_stren = []
    times = []

    for i in range(len(start_times)):
        hours = int(end_times[i].split(':')[0]) - int(start_times[i].split(':')[0])
        minutes = int(end_times[i].split(':')[1]) - int(start_times[i].split(':')[1])
        total_time = hours + (minutes/60)

        stren = total_time * int(stren_per_hour[i])
        times.append(total_time)
        real_stren.append(stren)
        
    total_stren = sum(real_stren)
    return total_stren, times, real_stren

def find_fatigue_score(total_stren, times, real_stren):
    sleeps = []
    sleep_times = []
    for i in range(len(real_stren)):
        if real_stren[i] == 0:
            sleeps.append(i)
            sleep_times.append(times[i])

    print(sleeps, sleep_times)

    total_sleep = sum(sleep_times)
    longest_sleep_time = max(sleep_times)
    longest_sleep = sleeps[sleep_times.index(longest_sleep_time)]

    print(total_sleep, longest_sleep, longest_sleep_time)

    return None

total_stren, times, real_stren = find_total_stren(["0:00", "6:00", "7:00", "7:30", "9:00", "10:00"], ["6:00", "7:00", "7:30", "9:00", "10:00", "12:00"], ["0", "1", "2", "1", "3", "0"])
print(total_stren, times, real_stren)
fatigue_score = find_fatigue_score(total_stren, times, real_stren)
print(fatigue_score)