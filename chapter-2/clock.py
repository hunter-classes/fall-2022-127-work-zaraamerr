# question 2.3 #

current_time_string = input("What is the current time in hours?")
waiting_time_string = input("How many hours are you going to wait?")

current_time_int = int(current_time_string)
waiting_time_int = int(waiting_time_string)

hours = current_time_int + waiting_time_int

timeofday = hours % 24

print(timeofday)