# coding: utf-8
import os
import sys

exe = './evaluateSwing'

argvs = sys.argv
argc  = len(argvs)

if (argc != 4): 
    print 'input: ' + exe + ' pressure [MPa] half_time [ms] repeat num'
    quit() 

pressure  = argvs[1]
half_time = argvs[2]
repeat_n  = int(argvs[3])

command = exe + ' ' + pressure + ' ' + half_time

for n in range(0,repeat_n):
    os.system(command)
