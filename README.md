# python_flock_ex1

Python 3で複数プロセスでflockを使って排他制御を行うサンプルコード。
flock()を使っているのでUNIXのみ動く。詳しくは`man 2 flock`参照。


# 動かし方

- init_cnt.py - カウンターを0に初期化
- inc_cnt.py - カウンターを10000増やす(排他制御なし)。並行で複数動かすと死ぬ。
- flock_inc_cnt.py - カウンターを10000増やす。並行で動かしても死なない。

```sh
# 期待通りに動く
./init_cnt.py ; ./inc_cnt.py

# 死ぬ。または30000にならない
./init_cnt.py ; ./inc_cnt.py & ./inc_cnt.py & ./inc_cnt.py

# 30000になる
./init_cnt.py ; ./flock_inc_cnt.py & ./flock_inc_cnt.py & ./flock_inc_cnt.py
```
