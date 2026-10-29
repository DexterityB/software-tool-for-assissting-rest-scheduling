def get_num_time(time):
    num_time = int(time.split(":")[0]) + ((int(time.split(":")[1]))/60)
    return num_time

def get_str_time(time):
    str_time = f"{round(time//1)}:{int((time % 1) * 60):02d}"
    return str_time

def shift_sleep(current_wake_up_time, task_time, days):
    num_curr = get_num_time(current_wake_up_time)
    num_goal = get_num_time(task_time) - 0.5

    time_change = (num_curr - num_goal)/days

    print(num_curr, num_goal, time_change)
    print(get_str_time(time_change))

shift_sleep("8:30", "4:00", 8)