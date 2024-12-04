# -*- coding: utf-8 -*-
import os

## 取得
# NOTE: __file__は絶対パスと相対パスになり得るためabspathで絶対パスに統一して使用するのがコツ
# スクリプト自身の絶対パスを取得
abs_path = os.path.abspath(__file__)
print(abs_path) # /Users/~/python_os_path/src/path.py

# 指定パス(abs_path)からディレクトリ名を取得
dir = os.path.dirname(abs_path)
print(dir) # /Users/~/python_os_path/src

# 指定パスからファイル名を取得
file = os.path.basename(abs_path)
print(file) # path.py

# 実行場所のパスを取得
exe_path = os.getcwd()
print(exe_path) # /Users/~/python_os_path


## 分割
# 指定パスからディレクトリ名とファイル名を分割
dir, file = os.path.split(abs_path)
print(dir) # /Users/~/python_os_path/src
print(file) # path.py

# 指定パスからファイル名と拡張子を分割
file, ext = os.path.splitext(abs_path)
print(file) # /Users/~/python_os_path/src/path
print(ext) # .py


## 結合
joined_path = os.path.join(dir, "path.py")
print(joined_path) # /Users/~/python_os_path/src/path.py


## 存在確認
is_path = os.path.exists(joined_path)
print(is_path) # True