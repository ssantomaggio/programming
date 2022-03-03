
number_of_days = int(input("Insert number of days: "))
number_of_hours = int(input("Insert number of hours: "))
number_of_minutes = int(input("Insert number of minutes: "))
number_of_seconds = int(input("Insert number of seconds: "))

minutes_in_seconds = number_of_minutes * 60
day_in_seconds = number_of_days * 24 * 60 * 60
hour_in_seconds = number_of_hours * 60 * 60

total_of_seconds = (day_in_seconds + hour_in_seconds + minutes_in_seconds + number_of_seconds)
print(total_of_seconds)