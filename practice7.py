# 7. Write a Python program to calculate the number of days between two dates.

from datetime import date

f_date = date(2024, 7, 4)
l_date = date(2024,7,10)

diff = l_date-f_date

print(diff.days,"Days")