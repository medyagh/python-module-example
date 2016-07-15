from b import *
from a import *


print ("hello from main.py")
print ("---"*13*2)
print ("""
import * from module a and b \n both have hello()
the one which was imported last wins the namespace\n""")
print ("---"*13*2)


print (hello())


print ("---"*13*2)
print ("notice the ASCII Logo outside the function ")
print ("---"*13*2)
