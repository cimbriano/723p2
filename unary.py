from parser import *
from util import *
from tree import *
from grammar import *

print str(timeFliesPCFG)
print timeFliesSent
print parse(timeFliesPCFG, timeFliesSent) # produced None , which is wrong