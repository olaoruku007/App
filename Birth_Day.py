
def get_day_of_week(date_string):
    date_object = date.fromisoformat(date_string)
    return date_object.weekday()

# Example usage:
date_string = input("What is your DOB? (YYYY-MM-DD)")
day = get_day_of_week(date_string)
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print("Your DOB is on a", weekdays[day])
