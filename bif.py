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

def remove_file(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)

seedLCG(1)
lcg_out_filename="lcg"
mersenne_out_filename="mersenne"
xoro_out_filename="xoroshiro"
rg = RandomGenerator(Xoroshiro128(1234))
remove_file("lcg.out")
remove_file("mers.out")
remove_file("xoro.out")


def init_input_file(file):
    file.write("type: d" + "\n")
    file.write("count: " + str(count) + "\n")
    file.write("numbit: 32" + "\n")


with open(lcg_out_filename, mode="w") as lcg_file:
    init_input_file(lcg_file)
    for i in range(count):
        lcg_file.write(str(lcg()) + "\n")
    lcg_file.close()

with open(mersenne_out_filename, mode="w") as mersenne_file:
    init_input_file(mersenne_file)
    for i in range(count):
        mersenne_file.write(str(random.uniform(0, 10000000)) + "\n")
    mersenne_file.close()

with open(xoro_out_filename, mode="w") as xoro_file:
    init_input_file(xoro_file)
    for i in range(count):
        xoro_file.write(str(rg.standard_normal()) + "\n")
    xoro_file.close()

log_lcg = open('lcg.out', 'a')
log_lcg.flush()  # <-- here's something not to forget!
m_log = open('mers.out', 'a')
x_log = open('xoro.out', 'a')
m_log.flush()  # <-- h
x_log.flush()  # <-- h

subprocess.Popen(["dieharder", "-d", "3", "-g", "202", "-f", lcg_out_filename], stdout=log_lcg, stderr=log_lcg)
subprocess.Popen(["dieharder", "-d", "15", "-g", "202", "-f", lcg_out_filename], stdout=log_lcg, stderr=log_lcg)
subprocess.Popen(["dieharder", "-d", "208", "-g", "202", "-f", lcg_out_filename], stdout=log_lcg, stderr=log_lcg)
subprocess.Popen(["dieharder", "-d", "206", "-g", "202", "-f", lcg_out_filename], stdout=log_lcg, stderr=log_lcg)
subprocess.Popen(["dieharder", "-d", "206", "-g", "202", "-f", mersenne_out_filename], stdout=m_log, stderr=m_log)
subprocess.Popen(["dieharder", "-d", "3", "-g", "202", "-f", mersenne_out_filename], stdout=m_log, stderr=m_log)
subprocess.Popen(["dieharder", "-d", "15", "-g", "202", "-f", mersenne_out_filename], stdout=m_log, stderr=m_log)
subprocess.Popen(["dieharder", "-d", "208", "-g", "202", "-f", mersenne_out_filename], stdout=m_log, stderr=m_log)
subprocess.Popen(["dieharder", "-d", "2", "-g", "202", "-f", xoro_out_filename], stdout=x_log, stderr=x_log)
subprocess.Popen(["dieharder", "-d", "3", "-g", "202", "-f", xoro_out_filename], stdout=x_log, stderr=x_log)
subprocess.Popen(["dieharder", "-d", "15", "-g", "202", "-f", xoro_out_filename], stdout=x_log, stderr=x_log)
subprocess.Popen(["dieharder", "-d", "206", "-g", "202", "-f", xoro_out_filename], stdout=x_log, stderr=x_log)
subprocess.Popen(["ls", "-l"])