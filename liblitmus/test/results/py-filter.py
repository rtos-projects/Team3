#!/usr/bin/env python

import re
import sys


total_bailout_overhead = int("0")
total_lowCrit_Abandoned = int("0")
total_task_released = int("0")
total_lowcrit_deadline_miss = int("0")
total_hicrit_deadline_miss = int("0")
iscore1 = int("0")
start_counter = int("0")
start_count = int("0")
task_released = int("0")
end_count = int("0")
pid = int("0")
priority = int("0")
mode = int("0")
criticality = int("0")
exec_time = int("0")
c_lo = int("0")
c_hi = int("0")
bfund = int("0")


info = {}
with open(sys.argv[1]) as input:

    for line in input:
        if re.match("(.*)P1(.*)", line):
            if re.match("(.*)(B|b)ailout_overhead(.*)", line):
                if start_counter > int("0") and task_released == int("1"):
                    junk1, junk3, junk, bailout_overhead = (item.strip() for item in line.split(':',4))
                    total_bailout_overhead += int(bailout_overhead)
            elif re.match("(.*)(A|a)bandoned(.*)", line):
               if start_counter > int("0") and task_released == int("1"):
                    total_lowCrit_Abandoned += int("1")
                    print line
    #		junk, bfund = (item.strip() for item in line.split('-', 2))
    #		bfund = int(bfund)
    #		print "bfund = [%d]" %bfund
            elif re.match("(.*)AN(.*)", line):
                if start_counter > int("0") and task_released == int("1"):
                    junk2, pid, priority, mode, criticality, exec_time, c_lo, c_hi = (item.strip() for item in line.split('-',7))
                    pid = int(pid)
                    priority = int(priority)
                    mode = int(mode)
                    criticality = int(criticality)
                    exec_time = int(exec_time)
                    c_lo = int(c_lo)
                    c_hi = int(c_hi)
                    if pid != int("0"):
                        if exec_time != int("0"):
                            print "PID:-[%d]" %pid, "priority:-[%d]" %priority, "mode:-[%d]" %mode, "Criticality:-[%d]" %criticality, "exec_time:-[%d]" %exec_time, "c_lo:-[%d]" %c_lo, "c_hi:-[%d]" %c_hi #, "bfund:-[%d]" %bfund
            elif re.match("(.*)bfund(.*)", line):
                if start_counter > int("0") and task_released == int("1"):
                    junk, bfund = (item.strip() for item in line.split('-', 2))
                    bfund = int(bfund)
                    print "bfund = [%d]" %bfund
            elif re.match("(.*)fpps_start(.*)", line):
                start_counter = int("1")
                start_count += int("1")
            elif re.match("(.*)released(.*)", line):
                task_released = int("1")
                total_task_released += int("1")
            elif re.match("(.*)fpps_end(.*)", line):
                end_count += int("1")
                if end_count == start_count :
                    start_counter = int("0")
                    task_released = int("0")
            elif re.match("(.*)(E|e)ntering(.*)", line):
                 if((start_counter > int("0")) and (task_released == int("1"))) is bool("true"):
                    junk, junk1, junk3 = (item.strip() for item in line.split(':',3))
                    print line
            elif re.match("(.*)hicrit_deadline_miss(.*)", line):
                total_hicrit_deadline_miss += int("1")
            elif re.match("(.*)lowcrit_deadline_miss(.*)", line):
                total_lowcrit_deadline_miss += int("1")
            else:
                (item.strip() for item in line.split())


print "total bailout overhead	:- " '%d' %total_bailout_overhead
print "total lowCrit Abandoned	:- " '%d' %total_lowCrit_Abandoned
print "total tasks released     :- " '%d' %total_task_released
#print "total hicrit deadline miss  :-" '%d' %total_hicrit_deadline_miss
#print "total lowcrit deadline miss :-" '%d' %total_lowcrit_deadline_miss
print 'info:'
