schedule = {}

print("Enter tasks one by one, Type 'done' when finished.")

while True:
    task = input("\nEnter task or type 'done' when finished: ").strip()
    if task.lower() == 'done':
        break

    key_to_check = task

    existing_value = schedule.get(key_to_check)

    if not existing_value:
        score = int(input(f"Enter strenuous score per hour for {key_to_check}: "))
        schedule[key_to_check] = score      

    time = int(input(f"Enter time spent on {key_to_check} in hours: "))
    schedule[key_to_check] += time * score - score

total = sum(schedule.values())

print("Schedule:", schedule) 
print(f"Total strenuous score for the day: {total}")
if total > 100:
    print("Warning: Your strenuous score is above the recommended limit for the day. Please drink caffine")