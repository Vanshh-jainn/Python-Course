import math
print(math.sqrt(16))

# two types of modules in python
# built in module
# External module

import os

# Creating your own module
import mymodule
mymodule.hello()

# to download external module we need to type (pip install "module name") in terminal
import requests
r = requests.get("https://www.google.com")
print(r.text)