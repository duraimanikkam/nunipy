"""
3. Weather forecasting organization wants to show is it day or night. So, write a
program for such organization to find whether is it dark outside or not.
Hint: Use time module.

"""

import time

mytime = time.localtime()
if mytime.tm_hour < 6 or mytime.tm_hour > 18:
    print ('It is DARK Outside')
else:
    print ('It is Not DARK Outside')