from os import popen
from sys import argv

# defined the variable
# targetfile = 'nohup.out'
# targetword = 'error'

targetFile = argv[2]
targetWord = argv[1]

totalLines = 0
linesNum = 0


# count total lines in file
def gettotal(filename):
    global totalLines
    for i in open(filename):
        totalLines += 1
    return totalLines


# count target lines in file
def targetwordis(filename, wordname):
    global linesNum
    target = 'grep -i %s %s' % (wordname, filename)
    for item in popen(target):
        print item
        linesNum += 1
    print "Here is '%s' %d lines." % (wordname, linesNum)


def counts():
    targetwordis(targetFile, targetWord)
    gettotal(targetFile)
    per = float(linesNum) / totalLines * 100
    print "targetWords rate is '%s %%' " % round(per, 2)


if __name__ == "__main__":
    counts()
# num_lines = sum(1 for line in targetlist)
