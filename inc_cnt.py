#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
カウンターを10000増やす(排他制御なし)
並行で複数動かすと死ぬ。

実行例(期待したとおり動く):
./init_cnt.py ; ./inc_cnt.py

実行例(死ぬ。または30000にならない):
./init_cnt.py ; ./inc_cnt.py & ./inc_cnt.py & ./inc_cnt.py
"""

LOOP_CNT = 10000
COUNT_FILE = "./var/count"


def increment_counter():
    with open(COUNT_FILE, "r+") as f:
        cnt = int(f.read()) + 1
        f.truncate(0)
        f.seek(0)
        f.write(str(cnt))
    return cnt


def main():
    for i in range(0, LOOP_CNT):
        cnt = increment_counter()
    return cnt


if __name__ == "__main__":
    print(main())
