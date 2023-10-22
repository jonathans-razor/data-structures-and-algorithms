from datetime import datetime
# Use AM/PM time format.
print(datetime.now().strftime("%b-%#d-%Y_%#I_%M_%S_%p"))