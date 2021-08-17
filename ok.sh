#!/bin/sh
# 30000になる
./init_cnt.py ; ./flock_inc_cnt.py & ./flock_inc_cnt.py & ./flock_inc_cnt.py
