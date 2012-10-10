from parser import *
from util import *
from tree import *
from grammar import *

print "Part I: Unary Rules"
print str(timeFliesPCFG)
print timeFliesSent
print parse(timeFliesPCFG, timeFliesSent) # produced None , which is wrong

print
print "Part II: Warming up with Time Flies"
myTree = parse(timeFliesPCFG2, timeFliesSent)
print "myTree: "
print myTree
print "desiredTimeFliesParse: "
print desiredTimeFliesParse
print evaluate(desiredTimeFliesParse, myTree)
