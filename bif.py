#!/bin/env python


import random
import subprocess
import os
import randomgen
from randomgen import RandomGenerator, Xoroshiro128

def seedLCG(initVal):
    global rand
    rand = initVal


def lcg():
    a = 1140671485
    c = 128201163
    m = 2 ** 24
    global rand
    rand = (a * rand + c) % m
    return rand / m


count = 10000000


seedLCG(1)
lcg_out_filename="lcg"
mersenne_out_filename="mersenne"
xoro_out_filename="mersenne"
rg = RandomGenerator(Xoroshiro128(1234))
os.remove("lcg.out")
os.remove("mers.out")
os.remove("xoro.out")

with open(lcg_out_filename, mode="w") as lcg_file:
    lcg_file.write("type: d" + "\n")
    lcg_file.write("count: " + str(count) + "\n")
    lcg_file.write("numbit: 32" + "\n")
    for i in range(count):
        lcg_file.write(str(lcg()) + "\n")
    lcg_file.close()

with open(mersenne_out_filename, mode="w") as mersenne_file:
    mersenne_file.write("type: d" + "\n")
    mersenne_file.write("count: " + str(count) + "\n")
    mersenne_file.write("numbit: 32" + "\n")
    for i in range(count):
        mersenne_file.write(str(random.uniform(0, 10000000)) + "\n")
    mersenne_file.close()

with open(xoro_out_filename, mode="w") as xoro_file:
    xoro_file.write("type: d" + "\n")
    xoro_file.write("count: " + str(count) + "\n")
    xoro_file.write("numbit: 32" + "\n")
    for i in range(count):
        xoro_file.write(str(rg.standard_normal()) + "\n")
    xoro_file.close()

log_lcg = open('lcg.out', 'a')
log_lcg.flush()  # <-- here's something not to forget!
m_log = open('mers.out', 'a')
x_log = open('xoro.out', 'a')
m_log.flush()  # <-- h
x_log.flush()  # <-- h

#subprocess.Popen(["dieharder", "-d", "0", "-g", "202", "-f", lcg_out_filename], stdout=log_lcg, stderr=log_lcg)
subprocess.Popen(["dieharder", "-d", "1", "-g", "202", "-f", lcg_out_filename], stdout=log_lcg, stderr=log_lcg)
subprocess.Popen(["dieharder", "-d", "2", "-g", "202", "-f", lcg_out_filename], stdout=log_lcg, stderr=log_lcg)
subprocess.Popen(["dieharder", "-d", "3", "-g", "202", "-f", lcg_out_filename], stdout=log_lcg, stderr=log_lcg)
subprocess.Popen(["dieharder", "-d", "4", "-g", "202", "-f", lcg_out_filename], stdout=log_lcg, stderr=log_lcg)
subprocess.Popen(["dieharder", "-d", "4", "-g", "202", "-f", lcg_out_filename], stdout=log_lcg, stderr=log_lcg)
subprocess.Popen(["dieharder", "-d", "5", "-g", "202", "-f", lcg_out_filename], stdout=log_lcg, stderr=log_lcg)
subprocess.Popen(["dieharder", "-d", "6", "-g", "202", "-f", lcg_out_filename], stdout=log_lcg, stderr=log_lcg)
#subprocess.Popen(["dieharder", "-d", "7", "-g", "202", "-f", lcg_out_filename], stdout=log_lcg, stderr=log_lcg)
subprocess.Popen(["dieharder", "-d", "14", "-g", "202", "-f", lcg_out_filename], stdout=log_lcg, stderr=log_lcg)
#subprocess.Popen(["dieharder", "-a", "-g", "202", "-f", lcg_out_filename], stdout=log_lcg, stderr=log_lcg)
#subprocess.Popen(["dieharder", "-d", "0", "-g", "202", "-f", mersenne_out_filename], stdout=m_log, stderr=m_log)
subprocess.Popen(["dieharder", "-d", "1", "-g", "202", "-f", mersenne_out_filename], stdout=m_log, stderr=m_log)
subprocess.Popen(["dieharder", "-d", "2", "-g", "202", "-f", mersenne_out_filename], stdout=m_log, stderr=m_log)
subprocess.Popen(["dieharder", "-d", "3", "-g", "202", "-f", mersenne_out_filename], stdout=m_log, stderr=m_log)
subprocess.Popen(["dieharder", "-d", "4", "-g", "202", "-f", mersenne_out_filename], stdout=m_log, stderr=m_log)
subprocess.Popen(["dieharder", "-d", "5", "-g", "202", "-f", mersenne_out_filename], stdout=m_log, stderr=m_log)
subprocess.Popen(["dieharder", "-d", "6", "-g", "202", "-f", mersenne_out_filename], stdout=m_log, stderr=m_log)
#subprocess.Popen(["dieharder", "-d", "7", "-g", "202", "-f", mersenne_out_filename], stdout=m_log, stderr=m_log)
subprocess.Popen(["dieharder", "-d", "14", "-g", "202", "-f", mersenne_out_filename], stdout=m_log, stderr=m_log)
#subprocess.Popen(["dieharder", "-a", "-g", "202", "-f", mersenne_out_filename], stdout=m_log, stderr=m_log)
#subprocess.Popen(["dieharder", "-d", "0", "-g", "202", "-f", xoro_out_filename], stdout=x_log, stderr=x_log)
subprocess.Popen(["dieharder", "-d", "1", "-g", "202", "-f", xoro_out_filename], stdout=x_log, stderr=x_log)
subprocess.Popen(["dieharder", "-d", "2", "-g", "202", "-f", xoro_out_filename], stdout=x_log, stderr=x_log)
subprocess.Popen(["dieharder", "-d", "3", "-g", "202", "-f", xoro_out_filename], stdout=x_log, stderr=x_log)
subprocess.Popen(["dieharder", "-d", "4", "-g", "202", "-f", xoro_out_filename], stdout=x_log, stderr=x_log)
subprocess.Popen(["dieharder", "-d", "5", "-g", "202", "-f", xoro_out_filename], stdout=x_log, stderr=x_log)
subprocess.Popen(["dieharder", "-d", "6", "-g", "202", "-f", xoro_out_filename], stdout=x_log, stderr=x_log)
subprocess.Popen(["dieharder", "-d", "14", "-g", "202", "-f", xoro_out_filename], stdout=x_log, stderr=x_log)
subprocess.Popen(["ls", "-l"])