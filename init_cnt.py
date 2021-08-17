#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
カウンターを初期化する
"""

COUNT_FILE = "./var/count"


def main():
    with open(COUNT_FILE, "w") as f:
        f.write(str(0))


if __name__ == "__main__":
    main()
