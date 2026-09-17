from automatic import find_total_stren, find_sleep_times

def main():
    times, real_stren = find_total_stren(["0:00", "6:00", "7:00", "7:30", "9:00", "10:00"], ["6:00", "7:00", "7:30", "9:00", "10:00", "12:00"], ["0", "1", "2", "1", "3", "0"])
    print("Times:", times, "Real Stren:", real_stren)
    total_sleep, longest_sleep, longest_sleep_time = find_sleep_times(times, real_stren)
    print("Total Sleep:", total_sleep, "Longest Sleep:", longest_sleep, "Longest Sleep Time:", longest_sleep_time)

if __name__ == "__main__":
    main()