# Print the calender of any year and any month

import calendar
print("**********CALENDER**********")
yy = int(input("Enter the year: "))
mm = int(input("Enter the month: "))
print(calendar.month(yy, mm))
