import csv
import platform

import sys
import falcon

import numpy as np
import pandas as pd

print("Operating System: " + platform.system() + platform.release())
print("Python Version: " + platform.python_version())
print("file run in:" + sys.argv[0])
print("←————————————————————————————————————————→")
print(f"Python Version: {sys.version}")

print(f"NumPy Version: {np.__version__}")
print(f"Pandas Version: {pd.__version__}")
print(f"csv Version: {csv.__version__}")
print(f"falcon Version: {falcon.__version__}")
print(sys.path)
