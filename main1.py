from b import *
from a import *


print ("hello from main.py")
print ("""
import * from module a and b \nand both have hello()
the one which was imported last wins the namespace\n\n""")


print (hello())
