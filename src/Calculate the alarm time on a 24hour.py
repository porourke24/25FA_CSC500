# Calculate the alarm time on a 24-hour clock

# Ask the user for the current time (in hours, 0-23)
current_time = int(input("Enter the current time (in hours, 0-23): "))

# Ask the user for number of hours to wait for the alarm
hours_to_wait = int(input("Enter number of hours to wait for the alarm: "))

# Calculate the time when the alarm will go off (24-hour clock)
alarm_time = (current_time + hours_to_wait) % 24

# Output the result
print("The alarm will go off at", alarm_time, "o'clock (24-hour time).")
