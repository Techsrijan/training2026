from datetime import *
from time import *

while True:
    x=datetime.now()
    print("\r",x.strftime("%H:%M:%S"),end='',flush=True)
    sleep(1)