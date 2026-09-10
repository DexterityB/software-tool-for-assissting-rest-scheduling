def find_total_strenuousness(start_times, end_times, strenuousness_per_hour):
    real_strenuousness = []
    times = []

    for i in range(len(start_times)):
        hours = int(end_times[i].split(':')[0]) - int(start_times[i].split(':')[0])
        minutes = int(end_times[i].split(':')[1]) - int(start_times[i].split(':')[1])
        total_time = hours + (minutes/60)

        strenuousness = total_time * int(strenuousness_per_hour[i])
        times.append(total_time)
        real_strenuousness.append(strenuousness)
        
    total_strenuousness = sum(real_strenuousness)
    return total_strenuousness, times, real_strenuousness

def find_fatigue_score(total_strenuousness, times, real_strenuousness):
    sleeps = []
    sleep_times = []
    for i in range(len(real_strenuousness)):
        if real_strenuousness[i] == 0:
            sleeps.append(i)
            sleep_times.append(times[i])

    print(sleeps, sleep_times)

    total_sleep = sum(sleep_times)
    longest_sleep_time = max(sleep_times)
    longest_sleep = sleeps[sleep_times.index(longest_sleep_time)]

    print(total_sleep, longest_sleep, longest_sleep_time)

    return None

total_strenuousness, times, real_strenuousness = find_total_strenuousness(["0:00", "6:00", "7:00", "7:30", "9:00", "10:00"], ["6:00", "7:00", "7:30", "9:00", "10:00", "12:00"], ["0", "1", "2", "1", "3", "0"])
print(total_strenuousness, times, real_strenuousness)
fatigue_score = find_fatigue_score(total_strenuousness, times, real_strenuousness)
print(fatigue_score)