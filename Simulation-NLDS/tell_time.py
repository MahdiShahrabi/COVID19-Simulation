import datetime
from time import gmtime, strftime
import time

def tell_time(msg=''):
    now = datetime.datetime.now() 
    print(msg)
    print ("Current time is: ",now.strftime("%H:%M:%S"))