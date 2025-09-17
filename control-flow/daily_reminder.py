# daily_reminder.py
# Asks about a single task, its priority, and whether it's time-bound,
# then prints a customized reminder using match-case + if.

# Ask the user for the task and details (prompts must match expected text)
task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Use match-case to handle the different priority levels
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. Try to finish it soon.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a medium priority task. Try to schedule it when you can.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        # If the user typed something else for priority
        if time_bound == "yes":
            print(f"Reminder: '{task}' requires immediate attention today!")
        else:
            print(f"Note: '{task}' doesn't have a recognized priority. Try high, medium, or low.")
