# import modules
from modules import time_stamp
from pathlib import Path

time_stamp("3:45")
path = Path()
for file in path.glob('*.*'):
    print(file)
