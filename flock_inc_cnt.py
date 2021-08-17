#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
カウンターを10000増やす(排他制御あり)
並行で複数動かしてもOK
"""
import fcntl

LOOP_CNT = 10000
COUNT_FILE = "./var/count"
LOCK_FILE = "/tmp/.flock_inc_cnt"


def increment_counter():

    with open(COUNT_FILE, "r+") as f:
        cnt = int(f.read()) + 1
        f.truncate(0)
        f.seek(0)
        f.write(str(cnt))
    return cnt


def flock_increment_counter():
    with open(LOCK_FILE, "w+") as lockf:
        fcntl.flock(lockf.fileno(), fcntl.LOCK_EX)
        cnt = increment_counter()
        fcntl.flock(lockf.fileno(), fcntl.LOCK_UN)
    return cnt


def main():
    for i in range(0, LOOP_CNT):
        cnt = flock_increment_counter()
    return cnt


if __name__ == "__main__":
    print(main())
