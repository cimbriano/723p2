from parser import *
from util import *
from tree import *
from grammar import *
from sys import *
from extractGrammar import *

def main(args):

	which_part = args[1] if len(args) == 2 else None

	if which_part == "1":  		partI()
	elif which_part == "2": 	partII()
	elif which_part == "3": 	partIII()
	elif which_part == "all":	all_parts()
	else: 						usage()
		

def partI():
	print "Part I: Unary Rules"
	print str(timeFliesPCFG)
	print timeFliesSent
	print parse(timeFliesPCFG, timeFliesSent) # produced None , which is wrong

def partII():
	print "Part II: Warming up with Time Flies"
	myTree = parse(timeFliesPCFG2, timeFliesSent)
	print "myTree: "
	print myTree
	print "desiredTimeFliesParse: "
	print desiredTimeFliesParse
	print evaluate(desiredTimeFliesParse, myTree)

def partIII():
	print "Part III: Parsing English"

	filename = 'wsj.dev'
	print "Data file: " + filename

	pcfg = computePCFG(filename)
	
	print "PCFG length: " + str(len(pcfg))
	print str(pcfg)

	print
	print

	print "wsj.train"
	pcfg = computePCFG('wsj.train')
	print "length: " + str(len(pcfg))
	print parse(pcfg, ['NN', 'VBZ', 'IN', 'DT', 'NN']) 
	print parse(pcfg, ['VBZ', 'NN', 'IN', 'DT', 'NN'])

	print
	print nonBinaryTree
	print binarizeTree(nonBinaryTree)
	print debinarizeTree(binarizeTree(nonBinaryTree))

	print evaluateParser(pcfg, 'wsj.dev')


def all_parts():
	partI()
	partII()
	partIII()

def usage():
	print "Bad argument"
	print "Include 1 2 3 or all"
	print "usage: test.py [ 1 | 2 | 3 ]"

if __name__ == '__main__':
	main(sys.argv)