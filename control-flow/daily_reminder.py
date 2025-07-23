#!/usr/bin/python3
"""
Daily Reminder System
Provides customized reminders for a single task based on priority and time sensitivity
"""

def daily_reminder():
    """Generate a task reminder based on priority and time sensitivity"""
    print("\nDAILY TASK REMINDER\n" + "="*20)
    
    task = input("Enter your task: ").strip()
    priority = input("Priority (high/medium/low): ").lower().strip()
    time_bound = input("Is it time-bound? (yes/no): ").lower().strip()
    
    # Validate inputs
    if priority not in ('high', 'medium', 'low') or time_bound not in ('yes', 'no'):
        print("Invalid input! Please try again with valid options.")
        return
    
    print("\n" + "="*20)  # Separator
    
    match priority:
        case "high":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
            else:
                print(f"Reminder: '{task}' is a high priority task. Please address it soon.")
        case "medium":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a medium priority task with a deadline today!")
            else:
                print(f"Reminder: '{task}' is a medium priority task. Schedule time for it.")
        case "low":
            if time_bound == "yes":
                print(f"Note: '{task}' has a soft deadline today, but is low priority.")
            else:
                print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
  
if __name__ == "__main__":
    daily_reminder()