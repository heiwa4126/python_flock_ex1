#!/bin/sh
# 死ぬ。または30000にならない
./init_cnt.py ; ./inc_cnt.py & ./inc_cnt.py & ./inc_cnt.py
